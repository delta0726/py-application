# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 1 Dash HTML Components
# Topic       : 3 表示画像を切り替えるアプリケーション
# Update Date : 2022/3/27
# Page        : P153 - P154
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - HTMLタグを使ってレイアウトに画像を取り込む
#   --- Dash HTML Componentsを使用するためPython記法でHTMLを操作することが可能


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-1-3_表示画像を切り替えるアプリケーション.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
from datetime import datetime

import dash
import dash_html_components as html
from dash.dependencies import Input, Output


# インスタンス生成
app = dash.Dash(__name__)

# スタイル設定
# --- ボタンを丸く表示する
b_style = {"height": 100, "width": 100, "borderRadius": "50%", "fontSize": 50}


# 1 レイアウトの作成 -----------------------------------------------------------

# ＜ポイント＞
# - レイアウトにImgタグで画像表示を行う
# - ボタンで画像を切り替える


app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("ボタンをクリックすると画像が変わります"),
                html.Img(id="bird-img", style={"height": 600}),
            ]
        ),
        html.Button(id="b-one", children="1", style=b_style),
        html.Button(id="b-two", children="2", style=b_style),
        html.Button(id="b-three", children="3", style=b_style),
    ],
    style={"width": "80%", "margin": "auto"},
)


# 2 コールバックの作成 -----------------------------------------------------------

# ＜ポイント＞
# - 押下されたボタンのidを判定することで表示する画像のパスを選択する


@app.callback(
    Output("bird-img", "src"),
    Input("b-one", "n_clicks"),
    Input("b-two", "n_clicks"),
    Input("b-three", "n_clicks"),
)
def update_image(c_one, c_two, c_three):
    selected_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    if selected_id == "b-two":
        return "assets/bird2.png"
    elif selected_id == "b-three":
        return "assets/bird3.png"
    else:
        return "assets/bird1.png"


# 3 アプリの起動 ------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
