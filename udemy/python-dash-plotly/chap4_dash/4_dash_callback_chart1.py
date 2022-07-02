# ******************************************************************************
# Course      : Python/Dash/Plotlyで簡単に機械学習WEBアプリを開発しよう
# Chapter     : 4 Dash入門
# Theme       : コールバックの仕組み（グラフ更新）
# Creat Date  : 2022/3/13
# Final Update: 2022/7/2
# URL         : https://www.udemy.com/course/python-dash-plotly/
# ******************************************************************************


# ＜概要＞
# - Dashにおけるコールバックの仕組みを確認する


# ＜実行＞
# - Edit Configurationから通常どおり実行
# - ターミナルから以下のコードで実行
# conda activate python-dash-plotly
# python .\chap4_dash\4_dash_callback_chart1.py


# ＜目次＞
# 0 準備
# 1 ウィジェットの設定
# 2 コールバックの定義
# 3 アプリの起動


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly_express as px
from dash.dependencies import Input, Output

# データロード
df = px.data.gapminder()
df = df.query('continent == "Asia"')

# インスタンス生成
app = dash.Dash()


# 1 レイアウトの設定 -------------------------------------------------------

# ＜ポイント＞
# - レイアウトではウィジェットを設置することになるが、引数が多くなりがちで全体の構造が見えにくくなる
#   --- 引数に与えるアイテムはなるべく予め変数として格納しておく


# アイテム
# --- リストに辞書型のアイテムをループで追加していく
year_options = []
for year in df['year'].unique():
    year_options.append({'label': str(year), 'value': year})

# レイアウト
# --- Inputで入力した値をDivに出力する
app.layout = html.Div([
    html.H1('コールバック2 - グラフ'),
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='select-year', options=year_options, value=df['year'].min()),
    html.Div(id='output_div_id')
])


# 2 コールバックの定義 --------------------------------------------------

# ＜ポイント＞
# - デコレータの中では名前空間にある変数(df)を参照することができる
#   --- デコレータで受け取るのはウィジェットで指定されたパラメータ
#   --- パラメータをもとにデコレータ内で集計された計算結果を返す（デコレータに大規模なコードは書きたくない）
#   --- メイン処理を実行する関数を作っておいて、デコレータ内で関数を呼び出して実行


@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='select-year', component_property='value')
)
def update_output_figure(selected_year):
    filtered_df = df[df['year'] == selected_year]
    figure = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', log_x=True, color='continent')
    return figure


# 3 アプリの起動---------------------------------------------------------

if __name__ == '__main__':
    app.run_server()
