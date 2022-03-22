# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 4 複数コンポーネントの配置
# Topic       : 1 Divコンポーネントのstyle引数を用いた配置
# Update Date : 2022/3/23
# Page        : P114 - P116
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Divコンポーネントを用いると横に複数のコンポーネントを配置することができる


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-4-1_multiple_style.py


# ＜目次＞
# 0 準備
# 1 style引数のためのCSS
# 2 レイアウトの作成
# 3 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html

# インスタンス生成
app = dash.Dash(__name__)


# 1 style引数のためのCSS -------------------------------------------------------

# ＜ポイント＞
# - Divコンポーネントのstyle引数に渡すためのCSSを定義する


# CSS辞書
# --- 1段目のボックス
div_style3 = {
    "width": "40%",
    "height": "250px",
    "backgroundColor": "lime",
    "margin": "5%",
    "display": "inline-block",
}

# CSS辞書
# --- 2段目のボックス
div_style4 = {
    "width": "29%",
    "height": "250px",
    "backgroundColor": "skyblue",
    "margin": "2%",
    "display": "inline-block",
}


# 2 レイアウトの作成 --------------------------------------------------------------

# ＜ポイント＞
# - Divコンポーネントのchildren引数には複数コンポーネントを格納することができる


app.layout = html.Div([
        # 1段目（2つの長方形）
        html.Div([html.Div(style=div_style3),
                  html.Div(style=div_style3)], id="first_leader"),
        # 2段目（3つの長方形）
        html.Div([html.Div(style=div_style4),
                  html.Div(style=div_style4),
                  html.Div(style=div_style4)], id="second_leader"),
    ], id="leader")


# 3 アプリ起動 -------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
