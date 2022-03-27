# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 9 Dashの追加コンポーネント
# Theme       : 3 Dash DAQ
# Topic       : 1 DashCanvasコンポーネント
# Update Date : 2022/3/27
# Page        : P197 - P200
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Dash DAQはデータ収集と管理を行うコンポーネントを提供する
#   --- 表示が大きいものが多いためサイドバーには向かないものが多い
#   --- メイン画面のコンテンツとしては有用かもしれない


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch09_dash_additional_components\9-3-1_計器を実装したアプリケーションの作成.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np

# インスタンス生成
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# 1 レイアウトの作成 -------------------------------------------------------------

app.layout = html.Div(
    [
        html.Div(
            [
                daq.PowerButton(
                    id="daq-powerbutton",
                    label="計器を動作させるボタン",
                    on=False,
                    size=100,
                    color="red",
                ),
                dcc.Interval(id="daq-interval", interval=1000, n_intervals=0),
            ]
        ),
        # 計器を並べる
        html.Div(
            [
                html.Div(
                    [html.H2("ゲージ"), daq.Gauge(id="guage1")], className="three columns",
                ),
                html.Div(
                    [html.H2("グラデュエートバー"), daq.GraduatedBar(id="guage2")],
                    className="three columns",
                ),
                html.Div(
                    [html.H2("タンク"), daq.Tank(id="guage3")], className="three columns",
                ),
                html.Div(
                    [html.H2("LEDディスプレイ"), daq.LEDDisplay(id="guage4")],
                    className="three columns",
                ),
            ],
            style={"margin": "auto"},
        ),
    ]
)


# 2 コールバックの作成 -----------------------------------------------------------

# ＜ポイント＞
# - コールバック オンとオフを管理するコールバック
# - コールバック 計器にランダムな値を返すコールバック


@app.callback(Output("daq-interval", "disabled"), Input("daq-powerbutton", "on"))
def guage_witch(buttonon):
    if buttonon:
        return False
    else:
        return True

@app.callback(
    Output("guage1", "value"),
    Output("guage2", "value"),
    Output("guage3", "value"),
    Output("guage4", "value"),
    Input("daq-interval", "n_intervals"),
)
def update_guages(n_intervals):
    return list(np.random.uniform(0, 10, 4))


# 3 アプリの起動 ------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
