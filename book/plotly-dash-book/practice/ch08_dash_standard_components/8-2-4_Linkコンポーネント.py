# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 2 Dash Core Component
# Topic       : 4 Linkコンポーネント
# Update Date : 2022/3/27
# Page        : P162 - P163
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - ページ遷移などに使用するリンクコンポーネント


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-4_Linkコンポーネント.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 ----------------------------------------------------------

app.layout = html.Div(
    [
        dcc.Link("/test", href="/test"),
        html.Br(),
        dcc.Link("/test2", href="/test2"),
        html.Br(),
        dcc.Link("/test3", href="/test3"),
        html.Br(),
        dcc.Link("home", href="/")
    ],
    style={"fontSize": 30, "textAlign": "center"}
)


# 2 アプリの起動 -------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
