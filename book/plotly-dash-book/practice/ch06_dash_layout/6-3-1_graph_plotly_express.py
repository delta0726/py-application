# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 3 グラフ配置
# Topic       : 1 Plotly Expressを用いたグラフ配置
# Update Date : 2022/3/22
# Page        : P112 - P113
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - プロットのコンポーネントはPlotly.expressかPlotly.pyで作成する
#   --- Plotly.expressはPlotly.pyのラッパー


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-3-1_graph_plotly_express.py


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 レイアウトの作成
# 3 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import plotly.express as px


# データロード
gapminder = px.data.gapminder()

# インスタンス生成
app = dash.Dash(__name__)


# 1 コンポーネントの作成 ---------------------------------------------------------

# データ抽出
gapminder2007 = gapminder[gapminder["year"] == 2007]

# プロット作成
item_plot = px.scatter(gapminder2007,
                       x="gdpPercap",
                       y="pop",
                       size="lifeExp",
                       color="continent",
                       hover_name="country",
                       log_x=True,
                       log_y=True,
                       title="Gapminder")


# 2 レイアウトの作成 ---------------------------------------------------------

# レイアウト作成
# --- 単一オブジェクトのみ
app.layout = dcc.Graph(figure=item_plot)


# 3 アプリ起動 ---------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
