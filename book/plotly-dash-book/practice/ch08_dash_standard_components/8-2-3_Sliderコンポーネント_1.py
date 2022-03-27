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
# - スライダーコンポーネントを作成する（コールバックなし）


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-3_Sliderコンポーネント_1.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -----------------------------------------------------------

# ＜ポイント＞
# - スライダーにはマーカーを付けることも可能


app.layout = html.Div(
    [
        # スライダの作成
        dcc.Slider(
            id="myslider",
            min=-10,
            max=100,
            step=1,
            value=50,
            marks={-10: {"label": "-10度", "style": {"color": "blue", "fontSize": 30},},
                   0: {"label": "0", "style": {"fontSize": 40}},
                   25: "25度",
                   50: {"label": "50度", "style": {"fontSize": 50}},
                   75: "75度",
                   100: {"label": "100度", "style": {"fontSize": 40, "color": "red"}}
                   },
            dots=True,
        )
    ],
    style={"width": "80%", "margin": "3% auto"},
)


# 2 アプリの起動 ----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
