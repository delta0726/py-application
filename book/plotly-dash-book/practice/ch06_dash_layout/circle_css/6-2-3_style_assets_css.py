# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 2 スタイル設定
# Topic       : 3 外部CSSを用いたスタイル設定
# Update Date : 2022/3/23
# Page        : P110
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Dashでは外部CSSをディレクトリに保存しておいて参照することができる
#   --- app.pyのカレントディレクトリにassetsフォルダを作って.cssを配置する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\circle_css\6-2-3_style_assets_css.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -----------------------------------------------------------

# className属性を設定
app.layout = html.Div([html.Div(className="circle")])


# 2 アプリ起動 -----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
