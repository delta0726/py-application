# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 9 Dashの追加コンポーネント
# Theme       : 2 Dash Bio
# Topic       : 2 サーコスプロット
# Update Date : 2022/3/27
# Page        : P194 - P197
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - サーコスプロットの作成例


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch09_dash_additional_components\9-2-2_サーコスプロット_2.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import json
from urllib.request import urlopen

import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# データロード
data = urlopen("https://raw.githubusercontent.com/"
    "plotly/dash-bio-docs-files/master/circos_graph_data.json"
).read()

# データ変換
circos_graph_data = json.loads(data)

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -------------------------------------------------------------

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.RadioItems(
                    id="radio-value",
                    options=[
                        {"label": "ヒストグラム外側表示", "value": "ヒストグラム外側表示"},
                        {"label": "ヒストグラム内側表示", "value": "ヒストグラム内側表示"},
                    ],
                    value="ヒストグラム外側表示",
                )
            ],
            style={"textAlign": "center"},
        ),
        dashbio.Circos(id="circos", layout=circos_graph_data["GRCh37"]),
    ],
    style={"width": "60%", "margin": "5% auto"},
)


# 2 コールバックの作成 -------------------------------------------------------------

@app.callback(Output("circos", "tracks"),
              Input("radio-value", "value"))
def update_graph(selected_value):
    if selected_value == "ヒストグラム外側表示":
        return [
            {
                "type": "HISTOGRAM",
                "data": circos_graph_data["histogram"],
            }
        ]
    return [
        {
            "type": "HISTOGRAM",
            "data": circos_graph_data["histogram"],
            "config": {"innerRadius": 40, "outerRadius": 300},
        }
    ]


# 3 アプリの起動 --------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
