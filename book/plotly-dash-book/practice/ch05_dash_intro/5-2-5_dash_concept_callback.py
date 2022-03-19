# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 5 Dash入門
# Theme       : 2-5 コールバック
# Creat Date  : 2022/3/20
# Final Update:
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - コールバックはアプリケーションの動的性質を定義する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch05_dash_intro\5-2-5_dash_concept_callback.py


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 レイアウト設定
# 3 コールバック
# 4 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# インスタンス生成
app = dash.Dash(__name__)


# 1 コンポーネントの作成 --------------------------------------------------------

# スタイル設定
# --- 横幅80％で中央寄せ、上下に5％の余白を作る
core_style = {"width": "80%", "margin": "5% auto"}

# ドロップダウンのアイテム
item_dropdown = [{"label": "white", "value": "white"},
                 {"label": "yellow", "value": "yellow"}]

# プロット定義
item_fig = px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])


# 2 レイアウト設定 -----------------------------------------------------------

# ＜ポイント＞
# - コールバックの入出力の属性指定はコンポーネントID(id)と属性名(引数名)を用いる
#   --- Inputの対象となるidを指定する（my-dropdown）
#   --- Outputの対象となるidを指定する（all-components）


# レイアウト構成
# --- 今回は3つのコンポーネントで構成
app.layout = html.Div([
    html.H1("Hello Dash", style={"textAlign": "center"}),
    dcc.Dropdown(id="my-dropdown",
                 options=item_dropdown,
                 value="white",
                 style=core_style),
    dcc.Graph(figure=item_fig,
              style=core_style)
], id="all-components")


# 3 コールバック --------------------------------------------------------------

# ＜ポイント＞
# - 今回はcore_styleの要素をコールバックで追加する
# - コールバックはDash.callbackデコレータでデコレートしたコールバック関数を用いて作成する
#   --- Input: id(my-dropdown)のvalue引数(white)を受け取る
#   --- Output: id(all-components)のstyle引数に値を渡す


@app.callback(
    Output("all-components", "style"),
    Input("my-dropdown", "value")
)
def update_background(selected_value):
    return {"backgroundColor": selected_value,
            "padding": "3%"}


# 4 アプリ起動 ----------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
