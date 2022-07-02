# ******************************************************************************
# Course      : Python/Dash/Plotlyで簡単に機械学習WEBアプリを開発しよう
# Chapter     : 3 Plotly Express
# Theme       : 基本的なPlotlyグラフ
# Creat Date  : 2022/3/12
# Final Update: 2022/7/2
# URL         : https://www.udemy.com/course/python-dash-plotly/
# ******************************************************************************


# ＜概要＞
# - Plotly Expressの使い方を確認する（Plotlyのラッパー）
# - PycharmにおけるPlotlyの表示方法としてpioでブラウザ表示する


# ＜目次＞
# 0 準備
# 1 データ概要の確認
# 2 プロット作成


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import plotly.express as px
import plotly.io as pio

# Plotlyをブラウザ出力
pio.renderers.default = 'browser'

# データ準備
df = px.data.gapminder()

# データ確認
df.columns
df.info()
df.describe()


# 1 データ概要の確認 -------------------------------------------------------

# 国数
country = df['country'].unique()
len(country)

# 地域
continent = df['continent'].unique()
len(continent)

# 地域と国をデータフレーム表示
# --- SciViewのボックスに変数を入力して内容を確認
country_map = df[['continent', 'country']].drop_duplicates()

# 大陸ごとの国数
name = 'Asia'
for name in df['continent'].unique():
    print(name, len(df.groupby('continent')['country'].unique()[name]))

# 大陸ごとの国数
df[['continent', 'country']].drop_duplicates().groupby(['continent']).count()

# 基準年
df['year'].unique()
len(df['year'].unique())

# 大陸ごとの国数
df.groupby('year')['country'].count()


# 2 プロット作成 --------------------------------------------------------------

# ＜ポイント＞
# - Plotly ExpressはPlotlyのラッパーで簡単な記述でプロット作成ができる

# データ確認
df[['continent', 'country', 'year', 'gdpPercap', 'lifeExp']]

# 散布図
fig1 = px.scatter(df, x='gdpPercap', y='lifeExp', log_x=True, color='continent')
fig1.show()

# レイアウト設定
# --- 引数名は辞書型をアンダースコアでつないだものになっている
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
fig2.show()

# 折れ線グラフ
# --- あらかじめデータを集計しておく
# --- X軸は時間、Y軸はX軸の単位で集計された連続値のデータ
df3 = df.groupby(['year', 'continent']).mean().reset_index()
fig3 =px.line(df3, x='year', y='lifeExp', title='Life Expectancy', color='continent')
fig3.show()

# 棒グラフ
# --- X軸はカテゴリカルデータ(時間を含む)、Y軸はX軸の単位で集計された連続値のデータ
df4 = df[df['country']=='Japan']
fig4 = px.bar(df4, x='year', y='pop', title='Japan pop')
fig4.show()

# 箱ひげ図
df5 = df[df['year']==2007]
fig5 = px.box(df5, x='continent', y='lifeExp')
fig5.show()

# バイオリン図
df6 = df[df['year']==2007]
fig6 = px.violin(df6, x='continent', y='lifeExp')
fig6.show()

# ヒストグラム
df7 = df[df['year']==2007]
fig7 = px.histogram(df7, x='lifeExp')
fig7.show()

# 円グラフ
df8 = df.assign(Count=1)
fig8 = px.pie(df8, names='continent', values='Count')
fig8.show()

# 階級区分図（コロプレス）
# --- ISOコードを用いてマッピング
df9 = df[df['year'] == 2007]
fig9 = px.choropleth(df, locations='iso_alpha', color='gdpPercap')
fig9.show()

# 複数枚プロット(Facet)
df10 = df.groupby(['continent', 'year']).mean().reset_index()
fig10 = px.line(df10, x='year', y='pop', facet_col='continent')
fig10.show()

# スライダーアニメーション
fig11 = px.choropleth(df, locations='iso_alpha', color='gdpPercap', animation_frame='year')
fig11.show()
