# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 2 スタイル設定
# Topic       : 2 コンポーネントを配置する
# Update Date : 2022/3/21
# Page        : P107 - P109
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - 複数のコンポーネントを用いたレイアウトを作成する場合はDivコンポーネントを用いる
#   --- divタグのラッパー（HTMLでコンテンツがひとかたまりであることを示す）


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-2-2_style_configure_margin.py


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html

# インスタンス生成
app = dash.Dash(__name__)


# 1 コンポーネントの作成 -------------------------------------------------------

# ＜ポイント＞
# - コンポーネントを中央配置にするためmarginを設定する
#   --- marginはコンポーネントの外側に余白を設定する


# HTMLの作成
# --- スタイル設定
app.layout = html.P(
    "こんにちは。昨日は雪が降りました。",
    style={
        "fontSize": 50,
        "color": "white",
        "backgroundColor": "#000000",
        "width": 400,
        "margin": "auto"
    },
)


# 2 アプリ起動 -----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
