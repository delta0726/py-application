# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 3 コールバック応用
# Topic       : 4 特定状態でのコールバックの更新停止
# Update Date : 2022/3/27
# Page        : P146 - P148
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - 前回2つに分けたコールバックを1つにまとめた実践的なケース


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-3-4_コールバックの更新停止_2.py


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


# 1 レイアウトの作成 -------------------------------------------------------------

# ＜ポイント＞
# - 散布図を作成する
# - 出力フォームにホバーが当たっているセルの情報をjsonで出力する
#   --- 上段のフォームは通常コールバック（起動時にホバーが当たってないためNullとなる）
#   --- 下段のフォームはPreventUpdateコールバック（起動時のNullを想定してコールバックを停止）
#   --- ホバーが当たったあとは同じ動作


app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        dcc.Graph(
            id="gapminder-g",
            figure=px.scatter(
                gapminder2007, x="gdpPercap", y="lifeExp", hover_name="country"
            ),
        ),
        html.P(
            id="hoverdata-p",
            style={
                "fontSize": 32,
                "textAlign": "center",
                "height": 100,
                "backgroundColor": "#e1eef6",
            },
        ),
        html.P(
            id="prevent-p",
            style={
                "fontSize": 32,
                "textAlign": "center",
                "height": 100,
                "backgroundColor": "#D7FFF1",
            },
        ),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)


# 2 コールバックの作成 ---------------------------------------------------------

# ＜ポイント＞
# - ホバーが当たっているかどうかで処理を分岐
# - Outputの戻り値1(PrecentUpdate)と戻り値2(通常出力)の2パターンを設定

@app.callback(
    Output("hoverdata-p", "children"),
    Output("prevent-p", "children"),
    Input("gapminder-g", "hoverData"),
)
def show_hover_data(hoverData):
    if hoverData is None:
        return (json.dumps(hoverData), dash.no_update)
    return json.dumps(hoverData), json.dumps(hoverData)


# 3 アプリ起動 --------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
