# ******************************************************************************
# Library     : Dash Bootstrap Components
# Category    : Examples
# Theme       : iris
# Update Date : 2022/3/20
# URL         : https://dash-bootstrap-components.opensource.faculty.ai/examples/iris/
# ******************************************************************************


# ＜概要＞
# - DashのUIの部品となるウィジェットを確認する


# ＜参考＞
# PyCharmIDEにPlotlyHTMLを埋め込む
# https://devdreamz.com/question/689434-embed-plotly-html-in-pycharm-ide


# ＜実行＞
# conda activate dash_bootstrap_components
# python .\example\iris.py


# ＜目次＞
# 0 準備
# 1 コントロールボックスの作成
# 2 レイアウトの作成
# 3 コールバックの作成
# 4 アプリ起動


# 0 準備 ------------------------------------------------------------------------------------------

# ライブラリ
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly
import plotly.graph_objs as go
from dash import Input, Output, dcc, html
from sklearn import datasets
from sklearn.cluster import KMeans

# データロード
iris_raw = datasets.load_iris()
iris = pd.DataFrame(iris_raw["data"], columns=iris_raw["feature_names"])

# インスタンス生成
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


# 1 コントロールボックスの作成 --------------------------------------------------------------------------------

# ＜ポイント＞
# - 以下の3つのコンポーネントのコントロールを行う
#   --- X軸に使用する特徴量
#   --- Y軸に使用する特徴量
#   --- k-meansに使用するクラスタ数


controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("X variable"),
                dcc.Dropdown(
                    id="x-variable",
                    options=[
                        {"label": col, "value": col} for col in iris.columns
                    ],
                    value="sepal length (cm)",
                ),
            ]
        ),
        html.Div(
            [
                dbc.Label("Y variable"),
                dcc.Dropdown(
                    id="y-variable",
                    options=[
                        {"label": col, "value": col} for col in iris.columns
                    ],
                    value="sepal width (cm)",
                ),
            ]
        ),
        html.Div(
            [
                dbc.Label("Cluster count"),
                dbc.Input(id="cluster-count", type="number", value=3),
            ]
        ),
    ],
    body=True,
)


# 2 レイアウトの作成 ---------------------------------------------------------------------------

# ＜ポイント＞
# - レイアウトは｢グラフ名｣と｢グラフ｣のみ


app.layout = dbc.Container(
    [
        html.H1("Iris k-means clustering"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dcc.Graph(id="cluster-graph"), md=8),
            ],
            align="center",
        ),
    ],
    fluid=True,
)


# 3 コールバックの作成 --------------------------------------------------------------------------

# ＜ポイント＞
# - Inputで設定情報を取得してクラスタリングを行いプロットを出力する


# デバッグ用
x = "sepal length (cm)"
y = "sepal width (cm)"
n_clusters = 3

@app.callback(
    Output("cluster-graph", "figure"),
    [
        Input("x-variable", "value"),
        Input("y-variable", "value"),
        Input("cluster-count", "value"),
    ],
)
def make_graph(x, y, n_clusters):
    km = KMeans(n_clusters=max(n_clusters, 1))
    df = iris.loc[:, [x, y]]
    km.fit(df.values)
    df["cluster"] = km.labels_

    centers = km.cluster_centers_

    data = [
        go.Scatter(
            x=df.loc[df.cluster == c, x],
            y=df.loc[df.cluster == c, y],
            mode="markers",
            marker={"size": 8},
            name="Cluster {}".format(c),
        )
        for c in range(n_clusters)
    ]

    data.append(
        go.Scatter(
            x=centers[:, 0],
            y=centers[:, 1],
            mode="markers",
            marker={"color": "#000", "size": 12, "symbol": "diamond"},
            name="Cluster centers",
        )
    )

    layout = {"xaxis": {"title": x}, "yaxis": {"title": y}}

    fig = go.Figure(data=data, layout=layout)

    # Debug
    #plotly.offline.plot(fig, filename='file.html')

    return fig


# make sure that x and y values can't be the same variable
def filter_options(v):
    """Disable option v"""
    return [
        {"label": col, "value": col, "disabled": col == v}
        for col in iris.columns
    ]


# functionality is the same for both dropdowns, so we reuse filter_options
app.callback(Output("x-variable", "options"), [Input("y-variable", "value")])(
    filter_options
)

app.callback(Output("y-variable", "options"), [Input("x-variable", "value")])(
    filter_options
)


# 4 アプリ起動 -----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)