# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 1 Plotly Express
# Theme       : 1-2 Plotly Expressとは
# Create Date : 2022/3/17
# Final Update:
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Plotly ExpressとはPlotly.pyの高水準ラッパー（インターフェースが簡素化）


# ＜実行＞
# VS-Code


# ＜目次＞
# 0 準備
# 1 プロット作成
# 2 インタラクティブ・プロット作成
# 3 ファセット・プロット
# 4 アニメーションプロット


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import plotly.express as px
import pandas as pd


# データ準備
tips = px.data.tips()
tips.head()


# 1 データの描画 --------------------------------------------------------------

# データ作成
df = pd.DataFrame([[1, 1], [2, 5], [3, 3]], columns=["x", "y"])

#
px.line(df, x="x", y="y").show()


# 2 データ型 -----------------------------------------------------------------


