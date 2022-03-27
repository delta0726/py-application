# ******************************************************************************
# Library     : Dash Bootstrap Components
# Category    : レイアウト・テーマ
# Theme       : Build the layout
# Update Date : 2022/3/28
# URL         : https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
# ******************************************************************************


# ＜概要＞
# - Navbarを使ってテーマを確認する


#  ＜テーマ一覧＞
# https://bootswatch.com/
# CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, MORPH, PULSE, QUARTZ,
# SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR.


# ＜実行＞
# conda activate dash_bootstrap_components
# python .\theme\theme_example.py


# 実行例 ---------------------------------------------------------------------------------

# ライブラリ
import dash
import dash_bootstrap_components as dbc

# インスタンス生成
# --- テーマを設定
app = dash.Dash(external_stylesheets=[dbc.themes.COSMO])


# レイアウト作成
# --- アラートに文字表示
app.layout = dbc.Container(
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="NavbarSimple",
        brand_href="#",
        color="primary",
        dark=True,
    ),
    className="p-5",
)

# アプリ起動
if __name__ == "__main__":
    app.run_server()
