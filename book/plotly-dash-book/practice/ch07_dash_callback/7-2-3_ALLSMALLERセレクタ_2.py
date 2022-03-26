# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 2 パターンマッチング・コールバック
# Topic       : 3 ALLSMALLERセレクタ
# Update Date : 2022/3/26
# Page        : P135 - P136
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - パターンマッチング・コールバックは条件に合ったコンポーネントを取得するコールバック
#   --- コールバックの連鎖を前提としている
# - --- ALLSMALLERセレクタはキーの値が現在より小さい要素を取得する（1つ前の状態を記憶する）


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-2-3_ALLSMALLERセレクタ_2.py


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
from dash.dependencies import Input, Output, State, ALL, ALLSMALLER, MATCH
import plotly.express as px

# データロード
gapminder = px.data.gapminder()

# インスタンス生成
app = dash.Dash(__name__)

# レイアウト設定
half_style = {"width": "50%", "display": "inline-block"}


# 1 レイアウトの作成 ------------------------------------------------------------

# ＜ポイント＞
# - ボタンを押下するとドロップダウンリストが2つ追加される
# - それぞれのドロップダウンリストの取得値からプロットを作成する


app.layout = html.Div(
    [
        html.Button("PUSH ME", id="my_button", n_clicks=0),
        html.Div(id="my_div", children=[]),
    ]
)


# 2 コールバックの作成 -----------------------------------------------------------

# ＜ポイント＞
# - Stateを設定することでボタンを押下した状態を検知している
# - ドロップダウンは2つ作成される（idは辞書のindexキーにn_clicksが値として格納されて固有化）
# - ドロップダウンの更新を検知してindexキーの選択された要素(ALLSMALLER)を取得してプロットを作成する
# - レイアウトを出力する


# コールバック1
@app.callback(
    Output("my_div", "children"),
    Input("my_button", "n_clicks"),
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
            dcc.Graph(id={"type": "my_graph", "index": n_clicks})
        ],
        style=half_style
    )
    children.append(new_layout)
    return children


# コールバック2
@app.callback(
    Output({"type": "my_graph", "index": MATCH}, "figure"),
    Input({"type": "my_dropdown", "index": ALLSMALLER}, "value"),
    Input({"type": "my_dropdown", "index": MATCH}, "value"),
    Input({"type": "my_dropdown2", "index": MATCH}, "value")
)
def update_graph(allsmaller_value, matching_value, selected_col):
    # データ選択
    # --- ドロップダウンで選択された全ての国名のデータを抽出
    selected_value = allsmaller_value + [matching_value]
    selected_countries = gapminder[gapminder["country"].isin(selected_value)]
    # プロット作成＆出力
    return px.line(selected_countries, x="year", y=selected_col, color="country")


# 3 アプリ起動 -----------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
