# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 4 複数コンポーネントの配置
# Topic       : 2 外部CSSを用いたスタイル設定
# Update Date : 2022/3/23
# Page        : P116 - P118
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - スクリプトを配置したディレクトリにassetsフォルダを作成して外部CSSを配置する
#   --- スクリプト内で配置したCSSの定義を参照する（.css自体を読込むわけではない）


# ＜参考＞
# Adding CSS & JS and Overriding the Page-Load Template
# https://dash.plotly.com/external-resources


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\external_css\6-4-2_multiple_external_css.py


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


# 1 レイアウトの作成 ----------------------------------------------------------

# ＜ポイント＞
# - className引数にCSS定義を指定する


app.layout = html.Div([
        html.H1("5つの四角形を並べたアプリケーション"),
        html.Div([
            html.Div(className="roundsqlime columns"),
            html.Div(className="roundsqlime columns")]),
        html.Div([
            html.Div(className="roundsqblue columns"),
            html.Div(className="roundsqblue columns"),
            html.Div(className="roundsqblue columns"),
            ])
])


# 2 アプリ起動 --------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
