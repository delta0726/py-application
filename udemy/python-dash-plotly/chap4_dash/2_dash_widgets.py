# ******************************************************************************
# Course      : Python/Dash/Plotlyで簡単に機械学習WEBアプリを開発しよう
# Chapter     : 4 Dash入門
# Theme       : DashのWidgets
# Creat Date  : 2022/3/13
# Final Update:
# URL         : https://www.udemy.com/course/python-dash-plotly/
# ******************************************************************************


# ＜概要＞
# - Dashで使用するWidgetsを確認する


# ＜実行＞
# - Edit Configurationから通常どおり実行
# - ターミナルから以下のコードで実行
# conda activate python-dash-plotly
# python .\chap4_dash\2_dash_widgets.py


# ＜目次＞
# 0 準備
# 1 ウィジェットの設定
# 2 アプリの起動


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html
import dash_core_components as dcc

# アプリの準備
# --- インスタンス生成
app = dash.Dash()


# 1 ウィジェットの設定 ----------------------------------------------------

# レイアウト
app.layout = html.Div(children=[
    html.H2(children='Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': '東京', 'value': 'Tokyo'},
            {'label': '大阪', 'value': 'Osaka'},
            {'label': '福岡', 'value': 'Fukuoka'}
        ]
    ),

    html.H2(children='Slider'),
    dcc.Slider(min=0, max=10, step=1),

    html.H2(children='Input Text'),
    dcc.Textarea(placeholder='ここに値を書いてね！',
                 style={'width': '50%'}),

    html.H2(children='Check List'),
    dcc.Checklist(options=[
        {'label': '東京', 'value': 'Tokyo'},
        {'label': '大阪', 'value': 'Osaka'},
        {'label': '福岡', 'value': 'Fukuoka'}
    ],
        value=['Tokyo', 'Osaka']),

    html.H2(children='Radio Button'),
    dcc.RadioItems(options=[
        {'label': '東京', 'value': 'Tokyo'},
        {'label': '大阪', 'value': 'Osaka'},
        {'label': '福岡', 'value': 'Fukuoka'}
    ],
        value='Osaka')
])


# 2 アプリの起動 --------------------------------------------------------

if __name__ == '__main__':
    app.run_server()
