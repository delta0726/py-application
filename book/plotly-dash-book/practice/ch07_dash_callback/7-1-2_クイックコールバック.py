# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 1 コールバックの基礎
# Topic       : 2 入出力を即座に反映するコールバック
# Update Date : 2022/3/25
# Page        : P125 - P126
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - コールバックのInputにボタンではなくコンポーネントを指定することでタイムリーに動作する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-1-2_クイックコールバック.py


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
from dash.dependencies import Input, Output

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの設定 -----------------------------------------------------------

# レイアウト
# --- 引数updatemodeに"drag"を渡し,動作を即座に反映するように設定
app.layout = html.Div(
    [
        html.H1(id="callback-output"),
        dcc.Slider(id="callback-input", value=0, updatemode="drag"),
    ],
    style={"textAlign": "center", "width": "60%", "margin": "auto"},
)


# 2 コールバックの設定 ----------------------------------------------------------

# ＜ポイント＞
# - Inputで受け取ったvalue引数の入力値がコールバック関数の引数となる
#   --- value引数の名前(value)とコールバック関数の引数名(num_value)は同じでなくてもよい


# コールバック
@app.callback(
    Output("callback-output", "children"),
    Input("callback-input", "value"),
)
def update_app(num_value):
    return num_value


# 3 アプリ起動 --------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
