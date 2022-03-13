# ******************************************************************************
# Course      : Python/Dash/Plotlyで簡単に機械学習WEBアプリを開発しよう
# Chapter     : 4 Dash入門
# Theme       : コールバックの仕組み（表・テーブルの挿入）
# Creat Date  : 2022/3/14
# Final Update:
# URL         : https://www.udemy.com/course/python-dash-plotly/
# ******************************************************************************


# ＜概要＞
# - データテーブルをアプリに挿入する


# ＜実行＞
# - Edit Configurationから通常どおり実行
# - ターミナルから以下のコードで実行
# conda activate python-dash-plotly
# python .\chap4_dash\6_dash_table.py


# ＜目次＞
# 0 準備
# 1 ウィジェットの設定
# 2 アプリの起動


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html
import dash_table
import plotly_express as px

# データロード
df = px.data.gapminder()

# インスタンス生成
app = dash.Dash()


# 1 レイアウトの設定 -------------------------------------------------------

# レイアウト
# --- Inputで入力した値をDivに出力する
app.layout = html.Div([
    html.H1('表の挿入'),
    html.H2('gapminder dataset', style={'textAlign': 'center'}),
    dash_table.DataTable(style_cell={'textAlign': 'center', 'width': '100px'},
                         fixed_rows={'header': True},
                         page_size=15,
                         sort_action='native',
                         filter_action='native',
                         columns=[{'name': col, 'id': col} for col in df.columns],
                         data=df.to_dict('records'),
                         fill_width=False)
])


# 2 アプリの起動---------------------------------------------------------

if __name__ == '__main__':
    app.run_server()
