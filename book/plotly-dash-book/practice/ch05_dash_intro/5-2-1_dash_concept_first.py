# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 5 Dash入門
# Theme       : 2 Dashの全体像
# Topic       : 1 コンポーネント
# Update Date : 2022/3/20
# Page        : P98 - P99
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Dashアプリの起動を確認する


# ＜Dashの構成要素＞
# - Dashのアプリケーションは以下の３要素で構成されている
#   --- コンポーネント（UIの部品）
#   --- レイアウト（コンポーネントを組み合わせてレイアウトを構成）
#   --- コールバック（アプリの動的性質を定義）


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch05_dash_intro\5-2-1_dash_concept_first.py


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


# 1 レイアウト設定 --------------------------------------------------------------

# コンポーネントをレイアウトに渡す
app.layout = html.H1("Hello Dash")


# 2 アプリ起動 -------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
