# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 3 コールバック応用
# Topic       : 1 画面遷移
# Update Date : 2022/3/26
# Page        : P137 - P138
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - ページごとにURLをを設定してコールバックで出力コンテンツを切り替えて画面遷移を実現している


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-3-1_画面遷移.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コンテンツの作成
# 3 コールバックの作成
# 4 アプリ起動


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

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -------------------------------------------------------------

app.layout = html.Div(
    [
        # URLの設定
        dcc.Location(id="my_location"),

        # コンテンツの表示
        html.Div(id="show_location",
                 style={"fontSize": 30, "textAlign": "center", "height": 400},),

        # Linkの設置
        html.Br(),
        dcc.Link("home", href="/"),
        html.Br(),
        dcc.Link("/graph", href="/graph"),
        html.Br(),
        dcc.Link("/table", href="/table"),
    ],
    style={"fontSize": 30, "textAlign": "center"},
)


# 2 コンテンツの作成 ----------------------------------------------------------------

# ＜ポイント＞
# - 各ページのコンテンツを定義する
#   --- 定義したコンテンツはレイアウトから参照される


# home
home = html.H1("irisデータ")

# graph
graph = dcc.Graph(
    figure=px.scatter(
        iris, x="sepal_width", y="sepal_length", color="species", title="irisグラフ"
    )
)

# table
table = dcc.Graph(
    figure=go.Figure(
        data=go.Table(
            header={"values": iris.columns},
            cells={"values": [iris[col].tolist() for col in iris.columns]},
        ),
        layout=go.Layout(title="irisデータテーブル"),
    )
)


# 3 コールバックの作成 -------------------------------------------------------------

# ＜ポイント＞
# - コールバックで画面遷移をコントロールする
#   --- 各pathnameごとに返すコンテンツを指定する
#   --- 条件にないpathnameはhomeを返す


@app.callback(Output("show_location", "children"),
              Input("my_location", "pathname"))
def update_location(pathname):
    if pathname == "/graph":
        return graph
    elif pathname == "/table":
        return table
    else:
        return home


# 4 アプリ起動 --------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
