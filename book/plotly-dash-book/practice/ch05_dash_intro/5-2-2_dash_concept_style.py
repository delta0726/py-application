# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 5 Dash入門
# Theme       : 2 Dashの全体像
# Topic       : 2 スタイル設定
# Update Date : 2022/3/20
# Page        : P99 - P100
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - コンポーネントのstyle引数に辞書型でCSSを渡すとスタイル設定がされる。
#   --- 辞書の中身はキーがCSSのプロパティ名、値がCSSのプロパティ値
#   --- キーはキャメルケースで定義する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch05_dash_intro\5-2-2_dash_concept_style.py


# ＜目次＞
# 0 準備
# 1 レイアウト設定
# 2 アプリ起動


# 0 準備 -----------------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウト設定 -------------------------------------------------------------

# ＜ポイント＞
# - コンポーネントのstyle引数にCSSで引数設定を行う
#   --- キーはキャメルケースで設定する

# タグの作成
# --- スタイル設定あり
app.layout = html.H1(
    "Hello Dash",
    style={"color": "red", "textAlign": "center"},
)


# 2 アプリ起動 --------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
