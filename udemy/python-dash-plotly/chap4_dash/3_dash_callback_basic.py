# ******************************************************************************
# Course      : Python/Dash/Plotlyで簡単に機械学習WEBアプリを開発しよう
# Chapter     : 4 Dash入門
# Theme       : コールバックの仕組み
# Creat Date  : 2022/3/13
# Final Update:
# URL         : https://www.udemy.com/course/python-dash-plotly/
# ******************************************************************************


# ＜概要＞
# - Dashにおけるコールバックの仕組みを確認する


# ＜実行＞
# - Edit Configurationから通常どおり実行
# - ターミナルから以下のコードで実行
# conda activate python-dash-plotly
# python .\chap4_dash\3_dash_callback_basic.py


# ＜目次＞
# 0 準備
# 1 ウィジェットの設定
# 2 アプリの起動


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


# インスタンス生成
app = dash.Dash()


# 1 レイアウトの設定 -------------------------------------------------------

# レイアウト
# --- Inputで入力した値をDivに出力する
app.layout = html.Div([
    html.H1('コールバック'),
    dcc.Input(id='input_test_id', value='initial value', type='text'),
    html.Div(id='output_div_id')
])

@app.callback(
    Output(component_id='output_div_id', component_property='children'),
    Input(component_id='input_test_id', component_property= 'value')
)
def update_output_div(input_value):
    return '入力は"{}"です。'.format(input_value)


# 2 アプリの起動 ---------------------------------------------------------

if __name__ == '__main__':
    app.run_server()
