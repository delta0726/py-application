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
# - サーコスプロットは要素間の関係性を示すプロットで応用範囲が広い


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch09_dash_additional_components\9-2-2_サーコスプロット_1.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_bio as dashbio
import dash_html_components as html

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 ------------------------------------------------------------

app.layout = html.Div(
    [
        dashbio.Circos(
            # ➊ グラフの円枠を作成する
            layout=[
                {"id": "1", "label": "1", "color": "lime", "len": 100},
                {"id": "2", "label": "2", "color": "pink", "len": 200},
                {"id": "3", "label": "3", "color": "purple", "len": 150},
                {"id": "4", "label": "4", "color": "skyblue", "len": 70},
                {"id": "5", "label": "5", "color": "yellow", "len": 180},
            ],
            # ➋ 円枠以外のグラフを作成する
            tracks=[
                {
                    # ➌ 作成するグラフの種類を設定する
                    "type": "CHORDS",
                    # ➍ グラフのデータを渡す
                    "data": [
                        {
                            "source": {"id": "1", "start": 50, "end": 100},
                            "target": {"id": "3", "start": 30, "end": 50},
                        },
                        {
                            "source": {"id": "1", "start": 30, "end": 50},
                            "target": {"id": "4", "start": 0, "end": 70},
                        },
                        {
                            "source": {"id": "2", "start": 100, "end": 200},
                            "target": {"id": "5", "start": 30, "end": 50},
                        },
                        {
                            "source": {"id": "3", "start": 100, "end": 150},
                            "target": {"id": "3", "start": 0, "end": 30},
                        },
                    ],
                    "opacity": 0.7,
                    "color": {"name": "color"},
                    "config": {
                        # マウスホバー時に表示するデータを設定する
                        "tooltipContent": {
                            "source": "source",
                            "sourceID": "id",
                            "target": "target",
                            "targetID": "id",
                            "targetEnd": "end",
                        }
                    },
                }
            ],
        )
    ]
)


# 2 アプリの起動 --------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
