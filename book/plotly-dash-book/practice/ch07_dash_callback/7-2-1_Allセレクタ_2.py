# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 2 パターンマッチング・コールバック
# Topic       : 1 ALLセレクタ（グラフ表示偏）
# Update Date : 2022/3/26
# Page        : P128 - P132
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - パターンマッチング・コールバックは条件に合ったコンポーネントを取得するコールバック
#   --- コールバックの連鎖を前提としている
# - --- ALLセレクタはキーが一致した全てのコンポーネントをコールバックで利用する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-2-1_Allセレクタ_2.py


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
from dash.dependencies import Input, Output, State, ALL
import plotly.express as px

# データロード
gapminder = px.data.gapminder()

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 ---------------------------------------------------------

# ＜ポイント＞
# - ボタンを押下するとドロップダウンリストを追加する
#   --- ドロップダウンリストを固定レイアウトにしていない点に注意
#   --- 追加したドロップダウンリストの要素に基づいてプロットを表示する


# レイアウトの作成
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="my_button"),
        html.Div(id="my_div", children=[]),
        html.Div(id="my_select")
    ]
)


# 2 コールバックの作成 ------------------------------------------------------

# ＜ポイント＞
# - Stateを設定することでボタンを押下した状態を検知している
# - ドロップダウンのidは辞書のindexキーにn_clicksが値として格納されて固有化されている
# - ドロップダウンの更新を検知してindexキーを全て(ALL)取得してリスト表示する


# コールバック1
# --- 基礎編と同様（ID名が異なるのみ）
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
            )
        ]
    )
    children.append(new_layout)
    return children


# コールバック2
@app.callback(
    Output("my_select", "children"),
    Input({"type": "my_dropdown", "index": ALL}, "value"),
    prevent_initial_call=True,
)
def update_graph(selected_values):
    # データ選択
    # --- ドロップダウンで選択された全ての国名のデータを抽出
    selected_countries = gapminder[gapminder["country"].isin(selected_values)]
    # プロット作成＆出力
    return dcc.Graph(
        figure=px.line(selected_countries, x="year", y="lifeExp", color="country")
    )


# 3 アプリ起動 ----------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
