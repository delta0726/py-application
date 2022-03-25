# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 1 コールバックの基礎
# Topic       : 3 複数入出力が存在するコールバック
# Update Date : 2022/3/26
# Page        : P126 - P128
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - コールバックでInputとOutputが複数存在するパターンを確認する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-1-3_複数入出力コールバック.py


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 レイアウトの作成
# 3 コールバックの作成
# 4 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# データロード
tips = px.data.tips()

# インスタンス生成
dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)


# 1 コンポーネントの作成 --------------------------------------------------------

# ドロップダウンリスト
# --- 曜日
item_dropdown_day = html.Div(
    [
        html.H4("曜日選択"),
        dcc.Dropdown(id="day_selector",
                     options=[{"value": dow, "label": dow} for dow in tips.day.unique()],
                     multi=True,
                     value=["Thur", "Fri", "Sat", "Sun"])
    ], className="six columns")

# ドロップダウンリスト
# --- グラフ種別
item_dropdown_graph = html.Div(
    [
        html.H4("グラフ選択"),
        dcc.Dropdown(id="graph_selector",
                     options=[{"value": "bar", "label": "bar"},
                              {"value": "scatter", "label": "scatter"}],
                     value="bar")
    ], className="six columns")


# 2 レイアウトの作成 --------------------------------------------------------------

app.layout = html.Div(
    [
        # レイアウト＆ドロップダウン
        html.H3(id="title", style={"textAlign": "center"}),
        html.Div(
            [
                item_dropdown_day,
                item_dropdown_graph,
            ],
            style={"padding": "2%", "margin": "auto"},
        ),
        # グラフ
        html.Div(
            [
                dcc.Graph(id="app_graph", style={"padding": "3%"}),
            ],
            style={"padding": "3%", "marginTop": 50},
        )
    ]
)


# 3 コールバックの作成 -----------------------------------------------------------

# ＜ポイント＞
# - Outputインスタンス,Inputインスタンスの順に配置
# - ドロップダウンの値(value)がInputに入って、Inputの順にコールバック関数に渡される


# デバッグ用
selected_days = ["Fri"]
selected_graph = "scatter"

@app.callback(
    Output("title", "children"),
    Output("app_graph", "figure"),
    Input("day_selector", "value"),
    Input("graph_selector", "value"),
)
def update_graph(selected_days, selected_graph):
    # データフレームの作成
    # --- 曜日でレコードを選択
    selected_df = tips[tips["day"].isin(selected_days)]
    # 選択されたグラフの種類により、タイトル表示データとグラフを作成
    if selected_graph == "scatter":
        title = "テーブル毎データ（散布図）"
        figure = px.scatter(selected_df, x="total_bill", y="tip", color="smoker", height=600)
    else:
        title = ("曜日ごとの売り上げ（棒グラフ）",)
        figure = px.bar(selected_df, x="day", y="total_bill", height=600)
    return title, figure


# 4 アプリ起動 ------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
