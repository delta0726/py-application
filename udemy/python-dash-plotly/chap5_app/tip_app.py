# ******************************************************************************
# Course      : Python/Dash/Plotlyで簡単に機械学習WEBアプリを開発しよう
# Chapter     : 5 Tipの額を予測するWebアプリ作成
# Theme       :
# Creat Date  : 2022/3/15
# Final Update:
# URL         : https://www.udemy.com/course/python-dash-plotly/
# ******************************************************************************


# ＜概要＞
# - 線形回帰モデルでTipsを予測するアプリを構築する


# ＜実行＞
# - Edit Configurationから通常どおり実行
# - ターミナルから以下のコードで実行
# conda activate python-dash-plotly
# python .\chap5_app\tip_app.py


# ＜目次＞
# 0 準備
# 1 機械学習モデリング
# 2 グラフの作成
# 3 アプリの作成
# 4 アプリの起動


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots
from sklearn.linear_model import LinearRegression

# データ準備
df = sns.load_dataset('tips')


# 1 機械学習モデリング ------------------------------------------------------

# 特徴量のダミー変換
use_data = df[['total_bill', 'size', 'time', 'tip']]
use_data = pd.get_dummies(use_data, drop_first=True)

# 学習用データ
X = use_data[['total_bill', 'size', 'time_Dinner']]
y = use_data[['tip']]

# モデル構築
model = LinearRegression()
model.fit(X, y)


# 2 グラフの作成 -----------------------------------------------------------

# サブプロット設定
tip_plots = make_subplots(rows=1, cols=3, start_cell='bottom-left')

# プロット
tip_plots.add_trace(go.Box(x=df['time'], y=df['tip'], name='time vs tip'), row=1, col=1)
tip_plots.add_trace(go.Scatter(x=df['total_bill'], y=df['tip'], mode='markers',
                               name='total_bill vs tip'), row=1, col=2)
tip_plots.add_trace(go.Scatter(x=df['size'], y=df['tip'], mode='markers',
                               name='size vs tip'), row=1, col=2)

# グラフレイアウト
tip_plots.update_layout(xaxis_title_text='Time', yaxis_title_text='Tips')
tip_plots.update_layout(xaxis2_title_text='Total Bill', yaxis2_title_text='Tips')
tip_plots.update_layout(xaxis3_title_text='Size', yaxis3_title_text='Tips')


# 3 アプリの作成---------------------------------------------------------

# インスタンス生成
app = dash.Dash()

# データテーブル
ui_data_table = \
    dash_table.DataTable(
        style_cell={'texAllign': 'center', 'width': '150px'},
        fill_width=False,
        fixed_rows={'header': True},
        page_size=10,
        filter_action='native',
        sort_action='native',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
    )

ui_input_total_bill = \
    dcc.Input(id='total_bill', placeholder='total_billを入力', type='text',
              style={'width': '20%'}, value='')

ui_input_size = \
    dcc.Input(id='size', placeholder='sizeを入力', type='text',
              style={'width': '20%'}, value='')

ui_input_time = \
    dcc.RadioItems(id='time',
                   options=[{'label': 'ランチ', 'value': 'Lunch'},
                            {'label': 'ディナー', 'value': 'Dinner'}],
                   value='Lunch',
                   labelStyle={'display': 'inline-block'})

# レイアウト
app.layout = html.Div([
    html.H1('チップの額を予測するアプリ', style={'texAllign': 'center'}),
    html.H2('分析用データ'),
    ui_data_table,
    html.P('データは{}件です。'.format(len(df))),
    html.H2('グラフ'),
    dcc.Graph(id='graph', figure=tip_plots, style={}),
    html.H2('予測用データのインプット'),
    ui_input_total_bill,
    ui_input_size,
    ui_input_time,
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.H2('チップの予測額'),
    html.Div(id='output-pred',
             style={'textAlign': 'center', 'fontsize': 30, 'color': 'red'})
])


# コールバック
@app.callback(
    Output('output-pred', 'children'),
    Input('submit-button', 'n_clicks'),
    [State('total_bill', 'value'),
     State('size', 'value'),
     State('time', 'value')]
)
def prediction(n_clicks, total_bill, size, time):
    if time == 'Lunch':
        dinner01 = 0
    else:
        dinner01 = 1

    if total_bill and size:
        value_df = pd.DataFrame([], columns=['Total bill', 'Size', 'Dinner flag'])
        record = pd.Series([total_bill, size, dinner01], index=value_df.columns, dtype='float64')
        value_df = value_df.append(record, ignore_index=True)
        Y_pred = model.predict(value_df)
        return_text = 'チップ額はおそらく' + str('{:.2g}'.format(Y_pred[0, 0]) + 'です。')
        return return_text
    else:
        return '入力値が入っていません。'


# 4 アプリの起動---------------------------------------------------------

if __name__ == '__main__':
    app.run_server()
