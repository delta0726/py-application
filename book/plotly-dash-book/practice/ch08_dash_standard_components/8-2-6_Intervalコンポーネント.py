# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 2 Dash Core Component
# Topic       : 6 Intervalコンポーネント
# Update Date : 2022/3/27
# Page        : P165 - P166
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - コールバックを一定時間ごとに更新するにはIntervalコンポーネントを使用する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-6_Intervalコンポーネント.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

# タイムスタンプの作成
# --- 開始時刻の取得
start = pd.Timestamp(datetime.datetime.now()).round("s")\
        - datetime.timedelta(seconds=300)

# データ作成
# --- 開始時刻から将来の株価を乱数で作成
# --- cumsumで累積値に変換
df = pd.DataFrame(
    {"price": np.random.randn(1000).cumsum()},
    index=pd.date_range(start, freq="s", periods=1000),
)

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -------------------------------------------------------------

# ＜ポイント＞
# - グラフコンポーネントを配置する
# - dcc.Intervalで一定時間ごとのコールバックを発動させる


app.layout = html.Div(
    [
        html.H1(id="realtime-title", style={"textAlign": "center"}),
        dcc.Graph(id="realtime-graph"),
        dcc.Interval(id="realtime-interval", interval=1000, max_intervals=100),
    ]
)


# 2 コールバックの作成 -----------------------------------------------------------

# ＜ポイント＞
# - dcc.Intervalで発動されたコールバックでグラフを更新する
#   --- 現時点から120秒前までのデータを取得しグラフを返す

@app.callback(
    Output("realtime-title", "children"),
    Output("realtime-graph", "figure"),
    Input("realtime-interval", "n_intervals"),
)
def update_graph(n_intervals):
    now = pd.Timestamp(datetime.datetime.now()).round("s")
    past = now - datetime.timedelta(seconds=120)
    plot_df = df.loc[past:now]

    return (
        f"live-update-chart: {now} / n_intervals: {n_intervals}",
        {"data": [go.Scatter(x=plot_df.index, y=plot_df["price"])]},
    )


# 3 アプリの起動 -----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
