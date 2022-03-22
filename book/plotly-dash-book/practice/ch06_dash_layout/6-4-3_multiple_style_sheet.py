# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 4 複数コンポーネントの配置
# Topic       : 3 スタイルシートをカスタマイズしたスタイル設定
# Update Date : 2022/3/23
# Page        : P118 - P119
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - 外部CSSを設定すると全体のCSSが定義されるが、個別コンポーネントのstyle引数を設定することで更新することも可能


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-4-3_multiple_style_sheet.py


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
external_sheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_sheet)


# 1 style引数のためのCSS ------------------------------------------------------

# 1段目用CSS辞書
div_style3 = {"height": "250px", "margin": "5%", "backgroundColor": "lime"}

# 2段目用CSS辞書
div_style4 = {"height": "250px", "backgroundColor": "skyblue"}


# 2 レイアウトの作成 ---------------------------------------------------------------

# ＜ポイント＞
# - style引数を設定して外部CSSを更新する


app.layout = html.Div([
        html.H1("5つの長方形を並べたアプリケーション（外部CSS）"),
        html.Div([
                html.Div(style=div_style3, className="five columns"),
                html.Div(style=div_style3, className="five columns")],
                id="first_leader"),
        html.Div([html.Div(style=div_style4, className="four columns"),
                  html.Div(style=div_style4, className="four columns"),
                  html.Div(style=div_style4, className="four columns")]
                 )
    ])


# 3 アプリ起動 ------------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
