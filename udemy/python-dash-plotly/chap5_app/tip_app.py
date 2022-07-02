# ******************************************************************************
# Course      : Python/Dash/Plotlyで簡単に機械学習WEBアプリを開発しよう
# Chapter     : 5 Tipの額を予測するWebアプリ作成
# Theme       : コールバックでモデルの予測値を取得する
# Creat Date  : 2022/3/15
# Final Update: 2022/7/2
# URL         : https://www.udemy.com/course/python-dash-plotly/
# ******************************************************************************


# ＜概要＞
# - 線形回帰モデルでTipsを予測するアプリを構築する
# - コンポーネントを分けてアプリ全体の見通しを良くする


# ＜実行＞
# - Edit Configurationから通常どおり実行
# - ターミナルから以下のコードで実行
# conda activate python-dash-plotly
# python .\chap5_app\tip_app.py


# ＜目次＞
# 0 準備
# 1 機械学習モデリング
# 2 グラフの作成
# 3 テーブルの作成
# 4 ウィジェットの作成
# 5 レイアウトの作成
# 6 コールバックの設定
# 7 アプリの起動


# 0 準備 -----------------------------------------------------------------

# ＜ポイント＞
# - 今回のアプリはボタンを押下したら実行されるようにするため｢State｣をインポートしておく


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
from plotly import offline


# データ準備
df = sns.load_dataset('tips')

# インスタンス生成
app = dash.Dash()


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

# 確認
# vars(model)


# 2 グラフの作成 -----------------------------------------------------------

# ＜ポイント＞
# - コールバックと関係ないプロットを作成する
#   --- 通常のPlotlyオブジェクトを作成してサブプロットで表示
#   --- plotlyオブジェクトとして作成する


# サブプロット設定
tip_plots = make_subplots(rows=1, cols=3, start_cell='bottom-left')

# プロット
tip_plots.add_trace(go.Box(x=df['time'], y=df['tip'], name='time vs tip'), row=1, col=1)
tip_plots.add_trace(go.Scatter(x=df['total_bill'], y=df['tip'], mode='markers',
                               name='total_bill vs tip'), row=1, col=2)
tip_plots.add_trace(go.Scatter(x=df['size'], y=df['tip'], mode='markers',
                               name='size vs tip'), row=1, col=3)

# グラフレイアウト
tip_plots.update_layout(xaxis_title_text='Time', yaxis_title_text='Tips')
tip_plots.update_layout(xaxis2_title_text='Total Bill', yaxis2_title_text='Tips')
tip_plots.update_layout(xaxis3_title_text='Size', yaxis3_title_text='Tips')

# 確認
# offline.plot(tip_plots)


# 3 テーブルの作成 ---------------------------------------------------------

# ＜ポイント＞
# - コールバックと関係ないテーブルを作成する
#   --- dash_tableオブジェクトとして格納する


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


# 4 ウィジェットの作成 ------------------------------------------------------

# ＜ポイント＞
# - ウィジェットはパーツ化できるので、個別にオブジェクトとして定義しておくほうが良い
#   --- レイアウト構成を考える際に、ウィジェットがパーツ化されているほうが全体が見えやすくなる


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


# 5 レイアウトの作成 ---------------------------------------------------

# ＜ポイント＞
# - ウィジェットなどのコンポーネントはなるべくパーツ化して全体の見通しが良くなるように務める
#   --- navbar / sidebar / body を使う際にも個々にパーツ化しておく


# レイアウト
app.layout = html.Div([
    # テキスト
    html.H1('チップの額を予測するアプリ', style={'texAllign': 'center'}),

    # テーブル（固定）
    html.H2('分析用データ'),
    ui_data_table,
    html.P('データは{}件です。'.format(len(df))),

    # グラフ（固定）
    html.H2('グラフ'),
    dcc.Graph(id='graph', figure=tip_plots, style={}),

    # ウィジェット
    html.H2('予測用データのインプット'),
    ui_input_total_bill,
    ui_input_size,
    ui_input_time,

    # 予測（コールバックあり）
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.H2('チップの予測額'),
    html.Div(id='output-pred',
             style={'textAlign': 'center', 'fontsize': 30, 'color': 'red'})
])


# 6 コールバックの設定 -----------------------------------------------------

# ＜ポイント＞
# - デコレータの中では名前空間にある変数を参照することができる
#   --- デコレータで受け取るのはウィジェットで指定されたパラメータ
#   --- パラメータをもとにデコレータ内で集計された計算結果を返す（デコレータに大規模なコードは書きたくない）
#   --- メイン処理を実行する関数を作っておいて、デコレータ内で関数を呼び出して実行


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


# 7 アプリの起動---------------------------------------------------------

if __name__ == '__main__':
    app.run_server()
