# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 3 コールバック応用
# Topic       : 3 グラフ上のマウス動作の活用
# Update Date : 2022/3/27
# Page        : P142 - P146
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - マウスモードをselectにしてマウスで選択した要素をselectedDataとして取得してアプリを作成する
#   --- マウスで範囲選択する動作でコールバックを発生させる（単一要素の選択ではない）


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-3-3_グラフ上のマウス操作_3.py


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


# 1 レイアウトの作成 ---------------------------------------------------------

# ＜ポイント＞
# - 散布図を作成する
# - 散布図の範囲選択された要素をselectedDataとしてコールバックに送る
#   --- コールバックの出力値をHTMLで表示する
#   --- マウス操作のセレクトモードを設定する


app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        dcc.Graph(
            id="gapminder-g",
            figure=px.scatter(
                gapminder2007,
                x="gdpPercap",
                y="lifeExp",
                hover_name="country",
                # ドラッグモードを"select"にする
                template={"layout": {"dragmode": "select"}},
            ),
        ),
        html.Div(
            [
                dcc.Graph(id="graph1", className="six columns"),
                dcc.Graph(id="graph2", className="six columns"),
            ]
        ),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)


# 2 コールバックの作成 --------------------------------------------------------

# ＜ポイント＞
# - Inputでpx.scatterのselectedDataを受け取る
#   --- 受け取ったデータを使って2種類の散布図を作成する(Outputは2つ)


@app.callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Input("gapminder-g", "selectedData"),
)
def show_hover_data(selectedData):
    if selectedData:
        selected_countries = [data["hovertext"] for data in selectedData["points"]]
        selected_df = gapminder[gapminder["country"].isin(selected_countries)]
        fig1 = px.line(selected_df, x="year", y="pop", color="country", title="各国の人口")
        fig2 = px.line(selected_df, x="year", y="lifeExp", color="country", title="各国の平均寿命")
        return fig1, fig2
    raise dash.exceptions.PreventUpdate


# 3 アプリ起動 --------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
