# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 5 Dash入門
# Theme       : 1 Dashとは
# Topic       : 1 Dashを用いたインタラクティブな可視化事例（テーブル）
# Update Date : 2022/3/20
# Page        : P96 - P97
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - Gapminderデータセットを用いた散布図のアプリ
#   --- Plotlyの散布図で国を選択することでcountry_nameを取得している点が興味深い


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch05_dash_intro\5-1-2_dash_sample_table.py


# ＜デバッグ＞
# 以下のコードにブレークポイントを入れてステップ実行
# - gapminder = px.data.gapminder()


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 レイアウト設定
# 3 コールバック設定
# 4 アプリ起動


# 0 準備 ------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
from dash_table import DataTable

# データロード
gapminder = px.data.gapminder()

# スタイル設定
# --- https://codepen.io/chriddyp/
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# インスタンス生成
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# 1 コンポーネントの作成 -----------------------------------------------------

# 固定プロット
plot_scatter = px.scatter(gapminder,
                          x="gdpPercap",
                          y="lifeExp",
                          size="pop",
                          color="continent",
                          animation_frame="year",
                          log_x=True,
                          size_max=70,
                          range_y=[20, 90],
                          hover_data=["country"],
                          template={"layout": {"clickmode": "event+select"}})


# 2 レイアウト設定 ----------------------------------------------------------

# ＜ポイント＞
# - Input: graph1でプロットを選択して国を指定
# - Output: graph2 / graph3 / tableに国ごとのデータを集計して出力


app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        html.H3("左側のグラフの要素をShift+マウスクリックで複数国が選択できます。"),
        html.Div([
            dcc.Graph(id="graph1",
                      figure=plot_scatter,
                      style={"width": "50%", "display": "inline-block", "height": 600}),
            html.Div([dcc.Graph(id="graph2", style={"height": 300}),
                      dcc.Graph(id="graph3", style={"height": 300})],
                     style={"width": "50%", "display": "inline-block", "height": 600})
        ]),
        html.Div([DataTable(id="table", export_format="csv", filter_action="native")],
                 style={"width": "80%", "margin": "auto"})
    ]
)


# 3 コールバック設定 -------------------------------------------------------------

# ＜ポイント＞
# - 起動時にはselectedDataは空のためif-raise文で例外を発生させて起動する
# - データがselectedDataに入力されるとコールバック処理を開始する


@app.callback(
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Output("table", "columns"),
    Output("table", "data"),
    Input("graph1", "selectedData"),
)
def update_graph(selectedData):
    if selectedData:
        # データセット選択
        # --- 国でデータ抽出
        selected_countries = [data["customdata"][0] for data in selectedData["points"]]
        selected_df = gapminder[gapminder["country"].isin(selected_countries)]

        # プロット作成
        fig1 = px.line(selected_df, x="year", y="pop", color="country", title="各国の人口")
        fig2 = px.line(selected_df, x="year", y="gdpPercap", color="country",
                       title="各国の1人当たりGDP")

        # コラム一覧作成
        columns = [
            {"name": col, "id": col, "deletable": True} for col in selected_df.columns
        ]
        return fig1, fig2, columns, selected_df.to_dict("records")
    raise dash.exceptions.PreventUpdate


# 4 アプリ起動 -------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
