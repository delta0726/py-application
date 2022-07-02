# ******************************************************************************
# Course      : Python/Dash/Plotlyで簡単に機械学習WEBアプリを開発しよう
# Chapter     : 2 Plotly
# Theme       : 基本的なPlotlyグラフ
# Create Date : 2022/3/13
# Final Update: 2022/7/2
# URL         : https://www.udemy.com/course/python-dash-plotly/
# ******************************************************************************


# ＜概要＞
# - Plotlyの使い方を確認する
# - PlotlyはJavaScriptベースのオブジェクトのため、パワーポイントなどにも使うことが添付することが可能


# ＜Plotlyの構成＞
# 1 figure : 描画領域
# 2 trace  : グラフの本体
# 3 layout : スタイル情報


# ＜実行＞
# VScodeのJuypyterにPlotlyオブジェクトを表示する


# ＜目次＞
# 0 準備
# 1 最初のグラフ作成
# 2 traceの設定
# 3 レイアウトを辞書型で設定
# 4 レイアウトを引数で設定
# 5 グラフの重ね書き
# 6 複数枚のグラフを描画


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# 1 最初のグラフ作成 ------------------------------------------------------

# 散布図の作成
graph_trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
fig = go.Figure(data=graph_trace)
fig.show()


# 2 traceの設定 ----------------------------------------------------------

# ＜ポイント＞
# - トレースはグラフのスタイル情報のことを指す
#   --- スタイル情報は作図関数の引数で設定する


# グラフ作成
graph_trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6],
                         mode='lines+markers',
                         marker={'size': 15, 'color': 'red'},
                         line={'color': 'black'})

# グラフ表示
fig = go.Figure(data=graph_trace)
fig.show()


# 3 レイアウトを辞書型で設定 ------------------------------------------------

# ＜ポイント＞
# - トレースはグラフのスタイル情報のことを指す
#   --- スタイル情報は作図関数の引数で設定する(辞書型で設定)


# グラフ作成
graph_trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6],
                         mode='lines+markers',
                         marker={'size': 15, 'color': 'red'},
                         line={'color': 'black'})

# レイアウト設定
graph_layout = go.Layout(width=600, height=500,
                         title={'text': 'test plot',
                                'font': {'family': 'times', 'size': 25, 'color': 'red'}},
                         xaxis={'title': {'text': 'X',
                                          'font': {'family': 'times', 'size': 15, 'color': 'blue'}},
                                'range': [0, 5]},
                         yaxis={'title': {'text': 'X',
                                          'font': {'family': 'times', 'size': 15, 'color': 'orange'}},
                                'range': [0, 10]})

# グラフ表示
fig = go.Figure(data=graph_trace, layout=graph_layout)
fig.show()


# 4 レイアウトを引数で設定 --------------------------------------------------

# ＜ポイント＞
# - レイアウトの辞書型表記は引数に変換することができる
#   --- 辞書のキーをアンダースコアで繋げたものが引数となる


# グラフ作成
graph_trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6],
                         mode='lines+markers',
                         marker={'size': 15, 'color': 'red'},
                         line={'color': 'black'})

# レイアウト設定
graph_layout = go.Layout(
    title_text='title',
    title_x=0.5,
    xaxis_title_text='X title',
    yaxis_title_text='Y title',
    xaxis_range=[0, 4],
    yaxis_range=[2, 8]
)

# グラフ表示
fig = go.Figure(data=graph_trace, layout=graph_layout)
fig.show()


# 5 グラフの重ね書き ---------------------------------------------------------

# ＜ポイント＞
# - add_traceを使うとグラフに重ね書きをすることができる

# プロット定義1
# --- 散布図 + ラインプロット
graph_trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6],
                         mode='lines+markers',
                         name='Line plot',
                         marker={'size': 15, 'color': 'black'},
                         line={"color": "black"}
                         )

# プロット定義2
# --- 棒グラフ
add_graph = go.Bar(x=[1, 2, 3], y=[4, 5, 6], name='Bar plot')

# チャート作成
fig = go.Figure(data=graph_trace)
fig.show()

# チャート追加
fig.add_trace(add_graph)
fig.show()

# レイアウト追加
fig.update_layout(
    title_text='title',
    title_x=0.5,
    xaxis_title_text='X title',
    yaxis_title_text='Y title',
    xaxis_range=[0, 4],
    yaxis_range=[2, 8]
)
fig.show()


# 6 複数枚のグラフを描画 ---------------------------------------------------

# レイアウト定義
fig = make_subplots(rows=2, cols=2, start_cell="bottom-left")

# プロット定義
p1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
p2 = go.Scatter(x=[7, 8, 9], y=[10, 11, 12])
p3 = go.Scatter(x=[13, 14, 15], y=[16, 17, 18])
p4 = go.Scatter(x=[19, 20, 21], y=[22, 23, 24])

# プロット埋め込み
fig.add_trace(p1, row=1, col=1)
fig.add_trace(p2, row=1, col=2)
fig.add_trace(p3, row=2, col=1)
fig.add_trace(p4, row=2, col=2)

# 出力
fig.show()
