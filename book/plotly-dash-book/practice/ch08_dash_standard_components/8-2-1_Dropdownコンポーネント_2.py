# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 2 Dash Core Component
# Topic       : 1 Dropdownコンポーネント
# Update Date : 2022/3/27
# Page        : P155 - P158
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - ドロップダウンリストを作成（アイテムを辞書内包表記で作成する）


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-1_Dropdownコンポーネント_2.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.express as px

# データロード
gapminder = plotly.data.gapminder()

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -----------------------------------------------------------

# ＜ポイント＞
# -  リストの選択肢を辞書内包表記で選択肢を作成する
#    --- リスト要素には表示キーと値キーを与える


app.layout = html.Div(
    [
        dcc.Dropdown(
            id="gapminder-dropdown",
            options=[{"label": c, "value": c} for c in gapminder["country"].unique()],
            value=["Japan", "China", "United States"],
            multi=True,
            style={"textAlign": "center"},
        )
    ],
    style={"width": "50%", "margin": "3% auto"},
)


# 2 アプリの起動 ---------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
