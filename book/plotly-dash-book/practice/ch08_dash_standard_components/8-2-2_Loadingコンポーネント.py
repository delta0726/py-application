# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 2 Dash Core Component
# Topic       : 2 Loadingコンポーネント
# Update Date : 2022/3/27
# Page        : P158 - P159
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Loadingコンポーネントはchildren引数に格納した値を出力する前にアニメーションスピナを表示する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-2_Loadingコンポーネント.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import time
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# インスタンス生成
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# 1 レイアウトの作成 -----------------------------------------------------------

# ＜ポイント＞
# - テキストボックスに値を入れてボタンを押下するとテキストが出力される
#   --- 出力時にアニメーションが表示される
#   --- dcc.Loadingのchildrenに出力値を渡している


app.layout = html.Div(
    [
        html.H3("Loading_Test"),
        dcc.Textarea(id="input_text", value="最初の値"),
        html.Button(id="input_1", children="Push"),
        dcc.Loading(
            id="loading_1",
            type="cube",
            children=[html.H1(id="loading", style={"margin": 100})],
        ),
    ],
    style={"textAlign": "center"},
)


# 2 コールバックの作成 ---------------------------------------------------------

# ＜ポイント＞
# - Stateを設定することでボタン押下してから動作させる


@app.callback(
    Output("loading", "children"),
    [Input("input_1", "n_clicks")],
    [State("input_text", "value")],
)
def input_trigger_spinner(n_clicks, value):
    time.sleep(3)
    return value


# 3 アプリの起動 --------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
