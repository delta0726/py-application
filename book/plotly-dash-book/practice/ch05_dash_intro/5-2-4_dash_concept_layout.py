# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 5 Dash入門
# Theme       : 2 Dashの全体像
# Topic       : 4 レイアウト
# Update Date : 2022/3/20
# Page        : P101 - P102
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - これまで作成したコンポーネントを組み合わせてレイアウトを構成する
#   --- アプリケーションの静的な見た目を決める作業


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch05_dash_intro\5-2-4_dash_concept_layout.py


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 レイアウト設定
# 3 アプリ起動


# 0 準備 -----------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# インスタンス生成
app = dash.Dash(__name__)


# 1 コンポーネントの作成 --------------------------------------------------------

# プロット定義
fig = px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])

# スタイル設定
# --- 横幅80％で中央寄せ、上下に5％の余白を作る
core_style = {"width": "80%", "margin": "5% auto"}


# 2 レイアウト設定 --------------------------------------------------------------

# ＜ポイント＞
# - リストにコンポーネントを並べてレイアウトに渡す
# - 一般的にコンポーネントは要素数が多くてコード量も多くなる
#   --- 全体が見やすくなるようにコードの書き方を工夫する必要がある

# レイアウト構成
# --- 今回は3つのコンポーネントで構成
layout = [html.H1("Hello Dash", style={"textAlign": "center"}),
          dcc.Dropdown(options=[{"label": "white", "value": "white"},
                                {"label": "yellow", "value": "yellow"}],
                       value="white",
                       style=core_style),
          dcc.Graph(figure=fig, style=core_style)]

# レイアウト定義
# --- リストに格納したレイアウトをDivクラスのchildren引数に渡す
app.layout = html.Div(children=layout)


# 3 アプリ起動 -----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
