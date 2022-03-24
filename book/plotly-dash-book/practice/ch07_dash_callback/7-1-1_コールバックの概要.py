# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 1 コールバックの基礎
# Topic       : 1 コールバックの概要
# Update Date : 2022/3/25
# Page        : P123 - P125
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - コールバックはアプリにインタラクティブ性を持たせるための仕組み


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-1-1_コールバックの概要.py


# ＜目次＞
# 0 準備
# 1 レイアウトの設定
# 2 コールバックの設定
# 3 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# インスタンス生成
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# 1 レイアウトの設定 ----------------------------------------------------------

# ＜ポイント＞
# - コールバックでコンポーネントを指定するためのIDを各コンポーネントに付与する


# レイアウト
# --- 各コンポーネントにIDを付ける
app.layout = html.Div(
    [
        html.H1(id="head-title"),
        dcc.Textarea(id="my-text-state",
                     value="initial value",
                     style={"width": "80%", "fontSize": 30}),
        html.Button(id="my-button", n_clicks=0, children="submit"),
    ],
    style={"margin": 50},
)


# 2 コールバックの設定 -------------------------------------------------------

# ＜ポイント＞
# - コールバック関数はDashクラスのcallbackメソッドでデコレータとして作成する
#   --- Output/Input/Stateの順に渡す
# - デコレータはコールバック関数の前後で動作する
#   --- Inputで情報を受け取り、Statusを確認して、Outputに出力する


# ＜コールバックの流れ＞
# 1 Buttonコンポーネントのn_click属性の値が変化
# 2 コールバック・デコレータの発動（Input: my-buttonコンポーネントからn_click引数を受け取る）
# 3 状態データの取得（Status： my-text-stateコンポーネントからvalue引数を受け取る）
# 4 コールバック関数の実行（出力値を取得）
# 5 コールバック・デコレータの発動（Output: head-titleコンポーネントのchildren引数に値を渡す）


# コールバック・デコレータの定義
# --- Output: 出力項目
# --- Input : 入力項目
# --- State : 状態項目
@app.callback(
    Output("head-title", "children"),
    Input("my-button", "n_clicks"),
    State("my-text-state", "value"),
)
# コールバック関数の定義
def update_title(n_clicks, value):
    return value


# 3 アプリ起動 ---------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
