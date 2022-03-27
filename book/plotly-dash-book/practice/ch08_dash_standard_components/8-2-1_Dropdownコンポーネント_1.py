# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 2 Dash Core Component
# Topic       : 1 Dropdownコンポーネント
# Update Date : 2022/3/27
# Page        : P155 - P158
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - ドロップダウンリストを作成


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-1_Dropdownコンポーネント_1.py


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


# 1 レイアウトの作成 ------------------------------------------------------------

app.layout = html.Div(
    [
        dcc.Dropdown(
            options=[
                {"label": "東京", "value": "tokyo"},
                {"label": "北海道", "value": "hokkaido"},
                {"label": "静岡", "value": "shizuoka"},
                {"label": "愛知", "value": "aichi"},
                {"label": "京都", "value": "kyoto"},
            ],
            value="kyoto",
            style={"textAlign": "center"},
        )
    ],
    style={"width": "80%", "margin": "3% auto"},
)


# 2 アプリの起動 ------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
