# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 7 Dashコールバック
# Theme       : 3 コールバック応用
# Topic       : 4 特定状態でのコールバックの更新停止
# Update Date : 2022/3/27
# Page        : P148 - P151
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - 連鎖コールバックは始めのコールバックの動作で2つめのコールバックの要素を操作する
#   --- 条件に応じてリストアイテムを変える場合などに使用する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch07_dash_callback\7-3-5_連鎖コールバック.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバック１の作成
# 3 コールバック２の作成
# 4 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State

# データロード
tips = px.data.tips()

# インスタンス生成
dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)


# 1 レイアウトの作成 -------------------------------------------------------------

# ＜ポイント＞
# - グラフ種別を選択すると以下の動作が行われる
#   --- ラジオボタンのアイテムの更新（コールバック1が発動）
#   --- グラフの変更（コールバック2が発動）
# - ラジオボタンを変更すると以下の動作が行われる
#   --- グラフの変更（コールバック2が発動）


app.layout = html.Div(
    [
        # アプリケーションのタイトル
        html.H1(id="head-title"),
        html.Div(
            [
                # ドロップダウンリスト
                # --- グラフ種別の選択
                html.P("グラフの種類の選択"),
                dcc.Dropdown(
                    id="graph-drop",
                    options=[
                        {"value": "bar", "label": "棒グラフ"},
                        {"value": "scatter", "label": "散布図"},
                    ],
                    value="bar",
                ),
                html.Div(
                    # ラジオボタン
                    # --- グラフ種別に応じて対象を変更（連鎖コールバック）
                    [html.P(id="selector-title"),
                     dcc.RadioItems(id="show-selector")]
                ),
            ],
            style={"float": "left", "width": "35%"},
        ),
        html.Div(
            # グラフ表示
            # --- 選択された種類のグラフを表示するGraph
            [dcc.Graph(id="show-graph")],
            style={"display": "inline-block", "width": "65%", "height": 800},
        ),
    ]
)


# 2 コールバック１の作成 ---------------------------------------------------

# ＜ポイント＞
# - 連鎖コールバックは条件に応じた値を戻り値として返す
#   --- 4つの返り値を作成

# ＜コールバック＞
# Output1： RadioItems（id="show-title"）の選択肢
# Output2： RadioItems（id="show-title"）の値
# Output3： H1（id="head-title"）の表示する文字
# Output4： P（id="selector-title"）の表示する文字
# Input  ： Dropdown（id="graph-drop"）で選択された値


@app.callback(
    Output("show-selector", "options"),
    Output("show-selector", "value"),
    Output("head-title", "children"),
    Output("selector-title", "children"),
    Input("graph-drop", "value"),
)
def update_selector(graph_type):
    if graph_type == "bar":
        return (
            [
                {"value": "total_bill", "label": "総額"},
                {"value": "sex", "label": "性別"},
                {"value": "smoker", "label": "喫煙 / 禁煙"},
                {"value": "time", "label": "時間帯（昼 / 夜）"},
            ],
            "total_bill",
            "チップデータ（棒グラフ）",
            "棒グラフ選択肢",
        )

    return (
        [
            {"value": "smoker", "label": "喫煙 / 禁煙"},
            {"value": "sex", "label": "性別"},
            {"value": "day", "label": "曜日"},
            {"value": "time", "label": "時間帯（昼 / 夜）"},
        ],
        "smoker",
        "チップデータ（散布図）",
        "散布図選択肢",
    )


# 3 コールバック２の作成 ----------------------------------------------------------

# ＜ポイント＞
# - グラフを出力するコールバック
#   --- コールバック1でグラフの条件が変更されることに対してコールバックを発動


@app.callback(
    Output("show-graph", "figure"),  #
    Input("show-selector", "value"),
    State("graph-drop", "value"),
)
def update_graph(selected_value, graph_type):
    if graph_type == "bar":
        return px.bar(
            tips,
            x="day",
            y="total_bill",
            color=selected_value,
            barmode="group",
            height=600,
            title=f"チップデータ棒グラフ（要素: {selected_value}）",
        )
    else:
        return px.scatter(
            tips,
            x="total_bill",
            y="tip",
            color=selected_value,
            height=600,
            title=f"チップデータ散布図（色: {selected_value}）",
        )


# 4 アプリ起動 -----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
