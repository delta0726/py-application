# ******************************************************************************
# Course      : Python/Dash/Plotlyで簡単に機械学習WEBアプリを開発しよう
# Chapter     : 4 Dash入門
# Theme       : Dashの使い方
# Creat Date  : 2022/3/13
# Final Update:
# URL         : https://www.udemy.com/course/python-dash-plotly/
# ******************************************************************************

# ＜概要＞
# - DashでWebアプリを起動する


# ＜実行＞
# - Edit Configurationから通常どおり実行
# - ターミナルから以下のコードで実行
# conda activate python-dash-plotly
# python .\chap4_dash\1_first_dash.py


# ＜目次＞
# 0 準備
# 1 レイアウトの設定
# 2 アプリの起動


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly_express as px


# データロード
df = px.data.gapminder()

# アプリの準備
# --- インスタンス生成
app = dash.Dash()


# 1 レイアウトの設定 ----------------------------------------------------

# ＜ポイント＞
# shinyでいうuiを設定する


# 準備
markdown_text = '''
# Test markdown
this is test markdown!
'''

# レイアウト
app.layout = html.Div(children=[
    html.H1(children='Hello Dash H1'),
    html.H2(children='Hello Dash H2'),
    html.H3(children='Hello Dash H3'),

    dcc.Graph(id='test_graph',
              figure=px.scatter(df, x='gdpPercap', y='lifeExp', log_x=True),
              style={}),

    dcc.Markdown(children=markdown_text)
])



# 2 アプリの起動 --------------------------------------------------------

# ＜ポイント＞
# - デバッグモードをTrueにしておくと、アプリの変更が


if __name__ == '__main__':
    app.run_server(debug=True)
