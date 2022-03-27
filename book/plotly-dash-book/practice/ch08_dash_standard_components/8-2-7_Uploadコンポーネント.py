# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 2 Dash Core Component
# Topic       : 7 Uploadコンポーネント
# Update Date : 2022/3/27
# Page        : P166 - P171
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Uploadコンポーネントを用いるとファイルのアップロードが可能となる
#   --- 使用頻度が低いのでコード整理のみ


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-2-7_Uploadコンポーネント.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 コールバックの作成
# 3 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import base64
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State

# インスタンス生成
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

# 共通スタイル設定
tab_selected_style = {
    "backgroundColor": "limegreen",
    "color": "white",
    "fontWeight": "bold",
}


# 1 レイアウトの作成 ------------------------------------------------------------------

app.layout = html.Div(
    [
        # ➊ Uploadコンポーネントを配置する。
        dcc.Upload(
            id="upload-csv",
            children=html.Div(
                ["Drag and Drop or ", html.A("Select CSV or Excel File")]
            ),
            style={
                "width": "80%",
                "height": "100px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "5% auto",
            },
        ),
        # テーブルとグラフの表示を切り替えるタブ
        dcc.Tabs(
            id="tabs",
            value="one",
            children=[
                # テーブルを表示するタブ
                dcc.Tab(
                    label="Table",
                    value="one",
                    selected_style=tab_selected_style,
                    children=[html.Div(id="upload-content")],
                ),
                # ドロップダウンとグラフを表示するタブ
                dcc.Tab(
                    label="Graph",
                    value="two",
                    selected_style=tab_selected_style,
                    children=[
                        html.Div(
                            [
                                dcc.Dropdown(id="table-dropdown", multi=True),
                                html.Div(id="update_graph"),
                            ]
                        )
                    ],
                ),
            ],
        ),
    ]
)


# 2 コールバックの作成 -----------------------------------------------------------------

@app.callback(
    Output("upload-content", "children"),
    Input("upload-csv", "contents"),
    State("upload-csv", "filename"),
)
def update_contents(contents, filename):
    if contents:
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
        # csvファイルとエクセルファイルのデータ読み込みの処理
        try:
            if filename.endswith(".csv"):
                df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
            elif filename.endswith(".xls") or filename.endswith(".xlsx"):
                df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div(["ファイルの処理中にエラーが発生しました"])
        # ファイル名をタイトル、読み込んだデータのテーブルを返り値とする
        return (
            html.H2(filename),
            dash_table.DataTable(
                id="table",
                data=df.to_dict("records"),
                columns=[{"name": i, "id": i} for i in df.columns],
            ),
        )


# ➌ グラフタブのドロップダウン作成用コールバック
@app.callback(
    Output("table-dropdown", "options"),
    Output("table-dropdown", "value"),
    Input("table", "columns"),
    Input("table", "derived_virtual_data"),
)
def update_dropdown(columns, rows):
    # テーブルのデータをデータフレームとする
    dff = pd.DataFrame(rows, columns=[c["name"] for c in columns])
    # 国名列にデータがあればドロップダウンの選択肢を作成し、初期値とともに返り値とする
    try:
        options = [{"value": i, "label": i} for i in dff["国名"].unique()]
        return options, [dff["国名"].unique()[0]]
    # 上記の処理ができない場合、コールバックを更新しない
    except:
        raise dash.exceptions.PreventUpdate


# ➍ ドロップダウンの選択を受けてグラフを作成するコールバック
@app.callback(
    Output("update_graph", "children"),
    Input("table", "columns"),
    Input("table", "derived_virtual_data"),
    Input("table-dropdown", "value"),
)
def update_graph(columns, rows, selected_countries):
    # テーブルのデータをデータフレームとする
    dff = pd.DataFrame(rows, columns=[c["name"] for c in columns])
    # ドロップダウンで国名が選択されていればグラフを作成する
    if not selected_countries:
        raise dash.exceptions.PreventUpdate

    dff["date"] = pd.to_datetime(dff["date"])
    dff = dff[dff["国名"].isin(selected_countries)]
    return dcc.Graph(figure=px.line(dff, x="date", y="value", color="国名"))


# 3 アプリの起動 --------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server()
