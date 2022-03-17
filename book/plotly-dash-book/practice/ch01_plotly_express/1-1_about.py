# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 1 Plotly Express
# Theme       : 1-1 Plotly Expressとは
# Creat Date  : 2022/3/17
# Final Update:
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Plotly ExpressとはPlotly.pyの高水準ラッパー（インターフェースが簡素化）


# ＜実行＞
# conda activate plotly-dash-book
# streamlit run .\practice\ch01_plotly_express\1-2_Introduction.py


# ＜目次＞
# 0 準備
# 1 プロット作成
# 2 インタラクティブ・プロット作成
# 3 ファセット・プロット
# 4 アニメーションプロット


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st


# データ準備
df = px.data.gapminder()

# データ確認
df.head()
df.info()


# 1 プロット作成 --------------------------------------------------------------

# プロット作成
df.plot.scatter(x="gdpPercap", y="lifeExp", logx=True, xlim=[100, 1e6])
# plt.show()


# 2 インタラクティブ・プロット作成 ------------------------------------------------

# 散布図（ベーシック）
fig1 = px.scatter(df, x="gdpPercap", y="lifeExp", log_x=True, hover_name="country")

# 散布図（装飾あり）
fig2 = px.scatter(df, x="gdpPercap", y="lifeExp", log_x=True,
                  hover_name="country", size="pop",  size_max=40,  color="continent")

# プロット表示
st.plotly_chart(fig1)
st.plotly_chart(fig2)


# 3 ファセット・プロット -----------------------------------------------------------

# プロット作成
facet_fig = px.scatter(df,x="gdpPercap", y="lifeExp", log_x=True,
                       hover_name="country", size="pop", size_max=40,
                       color="continent", facet_col="continent", width=800)

# プロット更新
facet_fig.update_xaxes(tickfont={"size": 8})

# プロット表示
st.plotly_chart(facet_fig)


# 4 アニメーションプロット --------------------------------------------------------

# プロット作成
animation_fig = px.scatter(df, x="gdpPercap", y="lifeExp", log_x=True,
                           hover_name="country", size="pop", size_max=40, color="continent",
                           facet_col="continent", width=800, animation_frame="year")

# プロット更新
animation_fig.update_xaxes(tickfont={"size": 8})

# プロット表示
st.plotly_chart(animation_fig)
