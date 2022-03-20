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
# - divコンポーネントで複数コンポーネントを用いたレイアウトを作成する


# ＜関連するCSS＞
# - display : 要素の表示方法を定義（初期値はinline）
# - float   : 要素に対してテキストやインライン要素が回り込めるように定義
# - margin  : マージン領域を設定する
# - padding : パディング領域を設定する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-2-2_style_configure_two.py


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
# - 通常は複数コンポーネントを並べた場合は縦に配置される
# - コンポーネントを横並びに配置する場合はdisplayで"inline-block"を指定する
# - コンポーネントの高さが異なる場合はデフォルトでは下揃えとなる
#   --- verticalAlignで"top"を指定することで上揃えとする


app.layout = html.Div(
    [
        html.P(
            "こんにちは。昨日は雪が降りました。",
            style={
                "fontSize": 50,
                "color": "white",
                "backgroundColor": "#000000",
                "width": "40%",
                "display": "inline-block",
            },
        ),
        html.P(
            "こんにちは。今日は晴れました。",
            style={
                "fontSize": 50,
                "color": "white",
                "backgroundColor": "red",
                "width": "40%",
                "display": "inline-block",
                "verticalAlign": "top",
            },
        ),
    ]
)


# 2 アプリ起動 ------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
