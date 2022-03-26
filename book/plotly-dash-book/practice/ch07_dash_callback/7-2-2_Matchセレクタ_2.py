# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 2 パターンマッチング・コールバック
# Topic       : 2 Matchセレクタ（グラフ表示偏）
# Update Date : 2022/3/26
# Page        : P132 - P135
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - MATCHセレクタで受け取った情報でグラフを更新する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-2-2_Matchセレクタ_2.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH
import plotly.express as px

# データロード
gapminder = px.data.gapminder()

# インスタンス生成
app = dash.Dash(__name__)

# 共通スタイル設定
half_style = {"width": "50%", "display": "inline-block"}


# 1 レイアウトの作成 ----------------------------------------------------------

# ＜ポイント＞
# - ボタンを押下するとドロップダウンリストが2つ追加される
# - それぞれのドロップダウンリストの取得値からプロットを作成する


# 2つのコンポーネントを持つレイアウト
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="add_drop", n_clicks=0),
        html.Div(id="my_div", children=[]),
    ]
)


# 2 コールバックの作成 ---------------------------------------------------------

# ＜ポイント＞
# - Stateを設定することでボタンを押下した状態を検知している
# - ドロップダウンは2つ作成される（idは辞書のindexキーにn_clicksが値として格納されて固有化）
# - ドロップダウンの更新を検知してindexキーの選択された要素(MATCH)を取得してプロットを作成する
# - レイアウトを出力する


# コールバック1
@app.callback(
    Output("my_div", "children"),
    Input("add_drop", "n_clicks"),
    State("my_div", "children"),
    prevent_initial_call=True,
)
def update_layout(n_clicks, children):
    new_layout = html.Div(
        [
            dcc.Dropdown(
                id={"type": "my_dropdown", "index": n_clicks},
                options=[{"label": c, "value": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks - 1],
            ),
            dcc.Dropdown(
                id={"type": "my_dropdown2", "index": n_clicks},
                options=[
                    {"label": col, "value": col} for col in gapminder.columns[3:6]
                ],
                value="lifeExp",
            ),
            dcc.Graph(id={"type": "my_graph", "index": n_clicks}),
        ],
        style=half_style,
    )
    children.append(new_layout)
    return children


# コールバック2
@app.callback(
    Output({"type": "my_graph", "index": MATCH}, "figure"),
    Input({"type": "my_dropdown", "index": MATCH}, "value"),
    Input({"type": "my_dropdown2", "index": MATCH}, "value"),
)
def update_graph(selected_value, selected_col):
    gap = gapminder[gapminder["country"] == selected_value]
    return px.line(gap, x="year", y=selected_col)


# 3 アプリ起動 ---------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
