# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 5 Dash入門
# Theme       : 1-1 Dashを用いたインタラクティブな可視化事例（散布図）
# Creat Date  : 2022/3/20
# Final Update:
# Page        : P96 - P97
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Gapminderデータセットを用いた散布図のアプリ


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch05_dash_intro\5-1-1_dash_sample_scatter.py


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 レイアウト設定
# 3 コールバック
# 4 アプリ起動


# 0 準備 ------------------------------------------------------------------

# ＜ポイント＞
# - Dashではスタイルシートを定義することができる


# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# データロード
gapminder = px.data.gapminder()

# スタイル設定
# --- https://codepen.io/chriddyp/
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# インスタンス生成
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# 1 コンポーネントの作成 -----------------------------------------------------------------

# ＜ポイント＞
# - ドロップダウンを同形式で複数作成するため処理を関数化しておく


# タイトルとドロップダウンを作成するコンポーネント
def header_and_dropdown(header_name, columns_name, dropdown_id):
    return html.Div(
        [
            html.H2(header_name),
            dcc.Dropdown(
                id=dropdown_id,
                options=[{"label": col, "value": col} for col in columns_name],
                value=columns_name[0],
            ),
        ],
        style={"width": "49%", "display": "inline-block"},
    )


# 2 レイアウト設定 ------------------------------------------------------------------------

app.layout = html.Div([
    html.H1("Gapminder Graph"),
    html.Div([header_and_dropdown("Select X axis", gapminder.columns[3:6], "x_axis"),
              header_and_dropdown("Select Y axis", gapminder.columns[3:6], "y_axis")]),
    dcc.Graph(id="graph")
])


# 3 コールバック ------------------------------------------------------------------------

# ＜ポイント＞
# - コールバックで散布図を作成してグラフオブジェクトをOutputに渡す


# コールバック
@app.callback(
    Output("graph", "figure"),
    Input("x_axis", "value"),
    Input("y_axis", "value")
)
def update_graph(x_axis_value, y_axis_value):
    return px.scatter(gapminder,
                      x=x_axis_value,
                      y=y_axis_value,
                      color="country",
                      log_x=True,
                      log_y=True)


# 4 アプリ起動 --------------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
