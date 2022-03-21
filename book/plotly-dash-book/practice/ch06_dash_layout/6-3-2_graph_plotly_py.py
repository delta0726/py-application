# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 3 グラフ配置
# Topic       : 2 Plotly.pyを用いたグラフ配置
# Update Date : 2022/3/22
# Page        : P113 - P114
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - プロットのコンポーネントはPlotly.expressかPlotly.pyで作成する
#   --- Plotly.pyはより精緻なプロットを作成することができる


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-3-2_graph_plotly_py.py


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 レイアウトの作成
# 3 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import plotly
import plotly.graph_objects as go


# データロード
gapminder = plotly.data.gapminder()

# インスタンス生成
app = dash.Dash(__name__)


# 1 コンポーネントの作成 --------------------------------------------------------

# データ抽出
gapminder2007 = gapminder[gapminder["year"] == 2007]

# オブジェクト生成
fig = go.Figure()

# プロット作成
# --- 地域ごとに散布図を作成
for c in gapminder2007.continent.unique():
    fig.add_trace(
        go.Scatter(
            x=gapminder2007.loc[gapminder2007["continent"] == c, "gdpPercap"],
            y=gapminder2007.loc[gapminder2007["continent"] == c, "pop"],
            name=c,
            mode="markers",
            marker={"size": gapminder2007.loc[gapminder2007["continent"] == c, "lifeExp"] / 2},
            text=gapminder2007.loc[gapminder2007["continent"] == c, "country"],
        )
    )

# レイアウト設定
fig.update_layout(
    xaxis={"type": "log", "title": "gdpPercap"},
    yaxis={"type": "log", "title": "pop"},
    title="Gapminder",
)


# 2 レイアウトの作成 ---------------------------------------------------------

# レイアウト作成
# --- 単一オブジェクトのみ
app.layout = dcc.Graph(
    figure=fig
)


# 3 アプリ起動 ---------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
