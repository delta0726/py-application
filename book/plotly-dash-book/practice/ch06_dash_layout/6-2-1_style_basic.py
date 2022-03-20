# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 2 スタイル設定
# Topic       : 1 コンポーネント自身のスタイル設定
# Update Date : 2022/3/21
# Page        : P106 - P107
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - スタイル設定はコンポーネントが持つstyle引数に辞書型で設定することで行うことができる
#   --- 辞書のキーにCSSのプロパティをキャメルケースで指定
#   --- 辞書の値にCSSのプロパティ値を指定


# ＜よく用いるCSSプロパティ＞
# - fontSize        : 文字の大きさをpxなどで定義
# - color           : 文字の色をカラーコード/色名称/RGBで指定
# - height          : 要素の高さをpxなどで定義
# - width           : 要素の幅を%/px/vwなどで定義
# - backgroundColor : 背景色を定義


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-2-1_style_basic.py


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


# 1 コンポーネントの作成 --------------------------------------------------------

# HTMLの作成
# --- レイアウト指定
app.layout = html.P(
    "こんにちは。昨日は雪が降りました。",
    style={
        "fontSize": 50,
        "color": "white",
        "backgroundColor": "#000000",
    },
)


# 2 アプリ起動 ----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
