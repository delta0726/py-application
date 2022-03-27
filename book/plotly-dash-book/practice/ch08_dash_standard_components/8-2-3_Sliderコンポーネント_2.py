# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 2 Dash Core Component
# Topic       : 3 Sliderコンポーネント
# Update Date : 2022/3/27
# Page        : P159 - P162
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - スライダーコンポーネントを作成する（コールバックあり）


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-3_Sliderコンポーネント_2.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -----------------------------------------------------------

app.layout = html.Div(
    [
        dcc.Slider(
            id="thisSlider",
            max=5,
            value=2,
            step=0.01,
            tooltip={"always_visible": False, "placement": "bottom"},
            updatemode="drag",
        ),
        html.P(
            id="pow-output", style={"marginTop": "5%", "fontSize": 30}
        )
    ],
    style={"width": "80%", "margin": "5% auto"},
)


# 2 コールバックの作成 -----------------------------------------------------------

@app.callback(
    dash.dependencies.Output("pow-output", "children"),
    dash.dependencies.Input("thisSlider", "value"),
)
def display_value(value):
    return f"数値: {value} | 10のべき乗: {10 ** value: .3f}"


# 3 アプリの起動 -----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
