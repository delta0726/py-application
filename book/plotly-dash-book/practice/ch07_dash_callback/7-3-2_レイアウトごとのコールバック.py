# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 3 コールバック応用
# Topic       : 2 レイアウトごとのコールバックが存在するアプリケーション
# Update Date : 2022/3/27
# Page        : P138 - P142
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - 画面ごとにコールバックを設定したアプリを作成する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-3-2_レイアウトごとのコールバック.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コンテンツの作成（homeページ）
# 3 コンテンツの作成（graphページ）
# 4 コンテンツの作成（tableページ）
# 5 コールバックの作成（ページ切り替え）
# 6 コールバックの作成（graphページ）
# 7 コールバックの作成（tableページ）
# 8 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

# データロード
iris = px.data.iris()

# 外部CSSの設定
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# インスタンス生成
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
)


# 1 レイアウトの作成 --------------------------------------------------------

app.layout = html.Div(
    [
        dcc.Location(id="my_location"),
        html.Div(id="show_location1", style={"height": 600}),
        html.Br(),
        dcc.Link("home", href="/"),
        html.Br(),
        dcc.Link("/graph", href="/graph"),
        html.Br(),
        dcc.Link("/table", href="/table"),
    ],
    style={"textAlign": "center"},
)


# 2 コンテンツの作成（homeページ） -------------------------------------------

# homeページ作成
home = html.H1("irisデータ")


# 3 コンテンツの作成（graphページ） ------------------------------------------

# グラフページ作成
graph = html.Div(
    [
        html.Div([
            html.Div([
                html.P("X軸: "),
                dcc.RadioItems(
                    id="x_axis_radio",
                    options=[{"label": col, "value": col} for col in iris.columns[:4]],
                    value="sepal_width"
                )],
                style={"display": "inline-block"}
            ),
            html.Div([html.P("Y軸: "),
                      dcc.RadioItems(
                          id="y_axis_radio",
                          options=[{"label": col, "value": col} for col in iris.columns[:4]],
                          value="sepal_length"
                      )],
                     style={"display": "inline-block"},
                )]
        ),
        dcc.Graph(id="radio-graph"),
    ]
)


# 4 コンテンツの作成（tableページ） ----------------------------------------------------

# テーブルページ作成
table = html.Div([
    html.Div([
        dcc.Dropdown(id="species-dropdown",
                     options=[{"value": col, "label": col} for col in iris.columns],
                     multi=True,
                     value=["sepal_length", "sepal_width"])
    ],style={"width": "60%", "margin": "auto"}),
    dcc.Graph(id="table"),
    ]
)


# 5 コールバックの作成（ページ切り替え）-----------------------------------------------

# ページ切り替え用コールバック
@app.callback(Output("show_location1", "children"),
              Input("my_location", "pathname"))
def update_location(pathname):
    if pathname == "/graph":
        return graph
    elif pathname == "/table":
        return table
    else:
        return home


# 6 コールバックの作成（graphページ）---------------------------------------------------

# グラフ更新用コールバック
@app.callback(
    Output("radio-graph", "figure"),
    Input("x_axis_radio", "value"),
    Input("y_axis_radio", "value"),
)
def update_graph(selected_x, selected_y):
    return px.scatter(
        iris,
        x=selected_x,
        y=selected_y,
        color="species",
        marginal_y="violin",
        marginal_x="box",
        title="irisグラフ",
    )


# 7 コールバックの作成（tableページ）----------------------------------------------------

# テーブル更新用コールバック
@app.callback(Output("table", "figure"),
              Input("species-dropdown", "value"))
def update_table(selected_value):
    iris_df = iris[selected_value]
    return go.Figure(
        data=go.Table(
            header={"values": iris_df.columns},
            cells={"values": [iris_df[col].tolist() for col in iris_df.columns]},
        ),
        layout=go.Layout(title="irisデータテーブル"),
    )


# 8 アプリ起動 -----------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
