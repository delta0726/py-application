# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 5 Dash入門
# Theme       : 2-3 グラフ作成
# Creat Date  : 2022/3/19
# Final Update:
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - グラフはGraphコンポーネントのfigure引数にplotlyで作成したプロットを渡す


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch05_dash_intro\5-2-3_dash_concept_graph.py


# ＜目次＞
# 0 準備
# 1 レイアウト設定
# 2 アプリ起動


# 0 準備 -----------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウト設定 --------------------------------------------------------------

# プロット作成
fig = px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])

# グラフ表示
# --- figureにplotlyで作成したプロットを渡す
app.layout = dcc.Graph(figure=fig)


# 2 アプリ起動 -----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
