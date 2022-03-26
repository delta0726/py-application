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
# python .\practice\ch07_dash_callback\7-2-3_ALLSMALLERセレクタ_1.py


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
from dash.dependencies import Input, Output, State, MATCH, ALLSMALLER
import plotly.express as px

# データロード
gapminder = px.data.gapminder()

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -------------------------------------------------------------

# ＜ポイント＞
# ドロップダウンと選択された値が追加される


app.layout = html.Div(
    [
        html.Button("PUSH ME", id="add_drop"),
        html.Div(id="show_drop", children=[])
    ],
    style={"width": "80%", "margin": "2% auto"},
)


# 2 コールバックの作成 -------------------------------------------------------------

# ＜ポイント＞
# - Stateを設定することでボタンを押下した状態を検知している
# - ドロップダウンのidは辞書のindexキーにn_clicksが値として格納されて固有化されている
# - ドロップダウンの更新を検知してindexキーの値より小さな要素(ALLSMALLER)を取得してリスト表示する


@app.callback(
    Output("show_drop", "children"),
    Input("add_drop", "n_clicks"),
    State("show_drop", "children"),
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
            html.P(id={"type": "text_show", "index": n_clicks}),
        ]
    )

    children.append(new_layout)
    return children


# コールバック2
@app.callback(
    Output({"type": "text_show", "index": MATCH}, "children"),
    Input({"type": "my_dropdown", "index": ALLSMALLER}, "value"),
)
def update_graph(selected_values):
    return str(selected_values)


# 3 アプリ起動 --------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
