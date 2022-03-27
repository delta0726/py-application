# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 2 Dash Core Component
# Topic       : 5 Locationコンポーネント
# Update Date : 2022/3/27
# Page        : P163 - P165
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Locationコンポーネントはアドレスバーに表示される値を取得する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-5_Locationコンポーネント.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -----------------------------------------------------------

# ＜ポイント＞
# - Locationコンポーネントの設置することでアドレスの取得が可能となる


app.layout = html.Div(
    [
        # Locationコンポーネントの設置
        dcc.Location(id="my_location"),
        # コールバックの出力先となる4つのDivクラス
        html.Div(id="show_location1", style={"fontSize": 30, "textAlign": "center"}),
        html.Div(id="show_location2", style={"fontSize": 30, "textAlign": "center"}),
        html.Div(id="show_location3", style={"fontSize": 30, "textAlign": "center"}),
        html.Div(id="show_location4", style={"fontSize": 30, "textAlign": "center"}),
        # Linkコンポーネントの設置
        html.Br(),
        dcc.Link("/test", href="/test"),
        html.Br(),
        dcc.Link("/test?what", href="/test?what"),
        html.Br(),
        dcc.Link("/test?what#dashhash", href="/test?what#dashhash"),
        html.Br(),
        dcc.Link("home", href="/"),
    ],
    style={"fontSize": 30, "textAlign": "center"},
)


# 2 コールバックの作成 -----------------------------------------------------------

# ＜ポイント＞
# - URL等のアイデムを結合して出力テキストを作成する


@app.callback(
    Output("show_location1", "children"),
    Output("show_location2", "children"),
    Output("show_location3", "children"),
    Output("show_location4", "children"),
    Input("my_location", "href"),
    Input("my_location", "pathname"),
    Input("my_location", "search"),
    Input("my_location", "hash"),
)
def update_location(url, pathname, search, hash):
    return (
        f"href={url}",
        f"pathname={pathname}",
        f"search={search}",
        f"hash={hash}"
    )


# 3 アプリの起動 -----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
