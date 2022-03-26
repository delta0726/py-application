# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 3 コールバック応用
# Topic       : 3 グラフ上のマウス動作の活用（マウスホバー）
# Update Date : 2022/3/27
# Page        : P142 - P146
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - hoverData属性を用いて、マウスカーソルを当てた散布図の要素のデータ表示するアプリを作成する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-3-3_グラフ上のマウス操作_1.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# データの作成
# --- gapminderデータの2007年分のみ
gapminder = px.data.gapminder()
gapminder2007 = gapminder[gapminder["year"] == 2007]

# インスタンス生成
dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)


# 1 レイアウトの作成 --------------------------------------------------

# ＜ポイント＞
# - 散布図を作成する
# - 散布図のホバーされた要素を検知してコールバックでHTMLで表示する

app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        dcc.Graph(
            id="gapminder-g",
            figure=px.scatter(
                gapminder2007, x="gdpPercap", y="lifeExp", hover_name="country"
            ),
        ),
        # ➎ ホバーデータを表示するPコンポーネント
        html.P(id="hoverdata-p", style={"fontSize": 32, "textAlign": "center"}),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)


# 2 コールバックの作成 ----------------------------------------------------

# ＜ポイント＞
# - Inputでpx.scatterのhoverData引数を受け取る
#   --- 受け取ったデータをjson形式に変換して出力する


@app.callback(
    Output("hoverdata-p", "children"),
    Input("gapminder-g", "hoverData")
)
def show_hover_data(hoverData):
    return json.dumps(hoverData)


# 3 アプリ起動 -----------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
