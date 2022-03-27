# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 2 Dash Core Component
# Topic       : 1 Dropdownコンポーネント（ラジオボタン）
# Update Date : 2022/3/27
# Page        : P155 - P158
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - ラジオボタンの作成
#   --- ドロップダウンリストと同様のオブジェクト構成


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-1_Dropdownコンポーネント_3.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.express as px

# データロード
gapminder = plotly.data.gapminder()

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -----------------------------------------------------------

app.layout = html.Div(
    [
        dcc.RadioItems(
            options=[
                {"label": "東京", "value": "東京"},
                {"label": "北海道", "value": "北海道"},
                {"label": "静岡", "value": "静岡"},
                {"label": "愛知", "value": "愛知"},
                {"label": "京都", "value": "京都"},
            ],
            value="京都",
            style={"textAlign": "center"},
        )
    ],
    style={"width": "80%", "margin": "3% auto"},
)


# 2 アプリの起動 ---------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
