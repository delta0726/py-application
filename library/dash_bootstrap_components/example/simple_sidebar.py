# ******************************************************************************
# Library     : Dash Bootstrap Components
# Category    : Examples
# Theme       : Simple sidebar
# Update Date : 2022/3/28
# URL         : https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
# ******************************************************************************


# ＜概要＞
# - サイドバー付きのレイアウトを作成する
#   --- サンプルではサイドバーでリンクを作っている
#   --- 実践ではウィジェットを配置する


# ＜実行＞
# conda activate dash_bootstrap_components
# python .\example\simple_sidebar.py


# ＜目次＞
# 0 準備
# 1 スタイル設定
# 2 サイドバーの作成
# 3 コンテンツの作成
# 4 レイアウトの作成
# 5 コールバックの作成
# 6 アプリ起動


# 0 準備 ------------------------------------------------------------------------------------------

# ライブラリ
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

# インスタンス生成
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


# 1 スタイル設定 ------------------------------------------------------------------------------------

# スタイル設定
# --- サイドバー
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


# スタイル設定
# --- コンテンツ
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


# 2 サイドバーの作成 -------------------------------------------------------------------------

# サイドバー
sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)



# 3 コンテンツの作成 ------------------------------------------------------------------------

# コンテンツ
content = html.Div(id="page-content", style=CONTENT_STYLE)


# 4 レイアウトの作成 -------------------------------------------------------------------------

# レイアウト
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# 5 コールバックの作成 ------------------------------------------------------------------------

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


# 6 アプリ起動 -----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(port=8888)
