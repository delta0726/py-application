# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 1 Dash HTML Components
# Topic       : 2 文字列を用いたアプリケーション
# Update Date : 2022/3/27
# Page        : P152 - P153
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - HTMLタグを使ってレイアウトを作成する
#   --- Dash HTML Componentsを使用するためPython記法でHTMLを操作することが可能


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-1-2_文字列を用いたアプリケーション.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html
from dash.dependencies import Input, Output

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -----------------------------------------------------------

# ＜ポイント＞
# - HTMLで文字列を出力
# - 文字列にカーソールを当ててクリックすると文字列が消える

# ＜コンポーネント＞
# - Div   ： コンテンツ分割
# - H1～H6： 見出し
# - P     ： テキストの段落


app.layout = html.Div(
    [
        html.H1("京都へようこそ！"),
        html.H2("おすすめ観光スポット"),
        html.P("- 清水寺", n_clicks=0, id="one"),
        html.P("- 八坂神社", n_clicks=0, id="two"),
        html.P("- 銀閣寺", n_clicks=0, id="three"),
        html.P("- 大文字", n_clicks=0, id="four"),
        html.P("- 鴨川", n_clicks=0, id="five"),
    ],
    style={"textAlign": "center"},
)


# 2 コールバックの作成 ----------------------------------------------------------

# ＜ポイント＞
# - ループでコールバックのidを変更して定義
#    --- ID名のリストからコールバックを作成
#    --- クリックカウンタが奇数ならOutputのhiddenにTrueを返す


for id_ in ["one", "two", "three", "four", "five"]:

    @app.callback(Output(id_, "hidden"),
                  Input(id_, "n_clicks"))
    def letter_disappear(n_clicks):
        if n_clicks % 2 == 1:
            return True


# 3 アプリの起動 ---------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
