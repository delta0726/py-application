# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 4 複数コンポーネントの配置
# Topic       : 4 複数コンポーネントを組み合わせた配置
# Update Date : 2022/3/24
# Page        : P119 - P121
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - CSSで実際の複数コンポーネントを配置したアプリを作成する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-4-4_multiple_combination.py


# ＜目次＞
# 0 準備
# 1 style引数のためのCSS
# 2 アイテムの作成
# 3 Divコンポーネントの作成
# 4 レイアウトの作成
# 5 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import plotly.express as px


# インスタンス生成
# --- 外部CSSの参照（全体のCSS設定）
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# 1 コンポーネントの共通CSSの設定 ------------------------------------------------

# 共通スタイルの作成
# --- 上の段のコンポーネント
div_style = {
    "width": "40%",
    "margin": "5%",
    "display": "inline-block",
    "verticalAlign": "top",
    "textAlign": "center"
}

# 共通スタイルの作成
# --- 下の段のコンポーネント
div_style2 = {
    "width": "29%",
    "margin": "2%",
    "verticalAlign": "top",
    "display": "inline-block"
}

# 共通スタイルの作成
# --- 下の段のコンポーネント
doc_style = {
    "fontSize": 20,
    "textAlign": "left",
    "backgroundColor": "lightgrey",
    "padding": "3%"
}


# 2 アイテムの作成 --------------------------------------------------------------

# グラフの作成
fig = px.line(
    x=[1, 2, 3, 4, 5],
    y=[[3, 2, 4, 1, 5], [2, 4, 3, 5, 3]],
    title="Dash Graph",
)
fig.data[0].name = "東京"
fig.data[1].name = '大阪'


# 3 Divコンポーネントの作成 --------------------------------------------------------

# ＜ポイント＞
# - コンポーネントの配置が複雑になる場合は個別のパーツをDivコンポーネントで作成しておく
#   --- 次のステップでパーツを組み合わせる形でDivコンポーネントを積み上げる


# コンポーネント（左上）
# --- ラインプロット
top_left = html.Div(
    [
        html.H1("Dashアプリケーション"),
        dcc.Markdown(
            """
            5つのDivクラスの領域に、複数のコンポーネントを並べました。

            - 左上はH1、Markdown、右上はGraph
            - 左下はH3、Dropdown、Slider、真ん中下はH3、TextArea、右下はH3、Checklist、RadioItems

            上記のコンポーネントをDivのchildren属性に渡しました。
            """,
            style=doc_style
        ),
    ],
    style=div_style,
)


# コンポーネント（右上）
# --- ラインプロット
top_right = html.Div(
    [
        dcc.Graph(figure=fig)
    ],
    style=div_style
)

# コンポーネント（左下）
# --- ラインプロット
bottom_left = html.Div(
    [
        html.H3("ドロップダウン"),
        dcc.Dropdown(
            options=[{"label": "東京", "value": "東京"}, {"label": "大阪", "value": "大阪"}],
            value="大阪",
        ),
        html.H3("スライダー"),
        dcc.Slider(min=-10, max=10, marks={i: f"label{i}" for i in range(-10, 11, 5)}),
    ],
    style=div_style2,
)

# コンポーネント（中央下）
# --- ラインプロット
bottom_mid = html.Div(
    [
        html.H3("テキストエリア入力"),
        html.Textarea(style={"height": 200, "width": "60%"}),
        html.Button("ボタン"),
    ],
    style=div_style2,
)

# コンポーネント（右下）
# --- ラインプロット
bottom_right = html.Div(
    [
        html.H3("選択肢", style={"textAlign": "center"}),
        # 2つのコンポーネントはスタイルシートを活用して横並びに
        dcc.Checklist(
            options=[
                {"label": "北海道", "value": "北海道"},
                {"label": "秋田", "value": "秋田"},
                {"label": "新潟", "value": "新潟"},
            ],
            value=["北海道", "新潟"],
            className="five columns",
        ),
        dcc.RadioItems(
            options=[
                {"label": "福岡", "value": "福岡"},
                {"label": "宮崎", "value": "宮崎"},
                {"label": "鹿児島", "value": "鹿児島"},
            ],
            value="鹿児島",
            className="five columns",
        ),
    ],
    style=div_style2,
)


# 4 レイアウトの作成 -----------------------------------------------------------

# ＜ポイント＞
# - 個別のDivコンポーネントをDivコンポーネントで組み合わせてレイアウトを作成する


app.layout = html.Div(
    children=[
        html.Div([top_left, top_right]),
        html.Div([bottom_left, bottom_mid, bottom_right]),
    ]
)


# 5 アプリ起動 -----------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
