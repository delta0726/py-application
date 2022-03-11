# ******************************************************************************
# Course      : Python/Streamlitによる機械学習WEBアプリの開発
# Chapter     : 4 Plotly Express
# Theme       : 基本的なPlotlyグラフ
# Creat Date  : 2022/3/12
# Final Update:
# URL         : https://www.udemy.com/course/pythonstreamlit/
# ******************************************************************************


# ＜概要＞
# - Plotly Expressの使い方を確認する
# - PycharmにおけるHTMLチャートの表示手段としてstreamlitを用いる


# ＜実行：ターミナル＞
# conda activate pythonstreamlit
# streamlit run .\chap5_Plotly_Express\1_plotly_express.py


# ＜目次＞
# 0 準備
# 1 データ概要の確認
# 2 プロット作成


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import plotly.express as px
import streamlit as st


# データ準備
df = px.data.gapminder()

# データ確認
df.info()
df.describe()


# 1 データ概要の確認 -------------------------------------------------------

# 国数
df['country'].unique()
len(df['country'].unique())

# 地域
df['continent'].unique()
len(df['continent'].unique())

# 大陸ごとの国数
for name in df['continent'].unique():
    print(name, len(df.groupby('continent')['country'].unique()[name]))

# 基準年
df['year'].unique()
len(df['year'].unique())

# 大陸ごとの国数
df.groupby('year')['country'].count()


# 2 プロット作成 --------------------------------------------------------------

# 散布図
fig1 = px.scatter(df, x='gdpPercap', y='lifeExp', log_x=True, color='continent')
st.plotly_chart(fig1)

# レイアウト設定
fig2 = px.scatter(df, x='gdpPercap', y='lifeExp', log_x=True, color='continent')
fig2.update_layout(
    title_text='Scatter Plot',
    title_x=0.5,
    xaxis_title_text='GDP per capita',
    yaxis_title_text='Life Expectancy',
    title_font_size=30,
    title_font_family='Times New Roman',
    title_font_color='black'
)
st.plotly_chart(fig2)

# 折れ線グラフ
df3 = df.groupby(['year', 'continent']).mean().reset_index()
fig3 =px.line(df3, x='year', y='lifeExp', title='Life Expectancy', color='continent')
st.plotly_chart(fig3)

# 棒グラフ
df4 = df[df['country']=='Japan']
fig4 = px.bar(df4, x='year', y='pop', title='Japan pop')
st.plotly_chart(fig4)

# 箱ひげ図
df5 = df[df['year']==2007]
fig5 = px.box(df5, x='continent', y='lifeExp')
st.plotly_chart(fig5)

# バイオリン図
df6 = df[df['year']==2007]
fig6 = px.violin(df6, x='continent', y='lifeExp')
st.plotly_chart(fig6)

# ヒストグラム
df7 = df[df['year']==2007]
fig7 = px.histogram(df7, x='lifeExp')
st.plotly_chart(fig7)

# 円グラフ
df8 = df.assign(Count = 1)
fig8 = px.pie(df8, names='continent', values='Count')
st.plotly_chart(fig8)
