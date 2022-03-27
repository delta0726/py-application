# ******************************************************************************
# Library     : Dash Bootstrap Components
# Category    : アイコン・テーマ
# Theme       : Build the layout
# Update Date : 2022/3/28
# URL         : https://dash-bootstrap-components.opensource.faculty.ai/docs/icons/
# ******************************************************************************


# ＜概要＞
# - Navbarを使ってアイコン・テーマを確認する


#  ＜テーマ一覧＞
# https://bootswatch.com/
# CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, MORPH, PULSE, QUARTZ,
# SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR.


# ＜実行＞
# conda activate dash_bootstrap_components
# python .\icon\Icon_Example.py


# 実行例 ---------------------------------------------------------------------------------

# ライブラリ
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


# インスタンス生成
# --- アイコンはテーマと別に設定することができる
app = dash.Dash(external_stylesheets=[dbc.themes.COSMO, dbc.icons.BOOTSTRAP])


alerts = html.Div(
    [
        dbc.Alert(
            [
                html.I(className="bi bi-info-circle-fill me-2"),
                "An example info alert with an icon",
            ],
            color="info",
            className="d-flex align-items-center",
        ),
        dbc.Alert(
            [
                html.I(className="bi bi-check-circle-fill me-2"),
                "An example success alert with an icon",
            ],
            color="success",
            className="d-flex align-items-center",
        ),
        dbc.Alert(
            [
                html.I(className="bi bi-exclamation-triangle-fill me-2"),
                "An example warning alert with an icon",
            ],
            color="warning",
            className="d-flex align-items-center",
        ),
        dbc.Alert(
            [
                html.I(className="bi bi-x-octagon-fill me-2"),
                "An example danger alert with an icon",
            ],
            color="danger",
            className="d-flex align-items-center",
        ),
    ]
)


app.layout = dbc.Container(
    alerts,
    className="p-5",
)


# アプリ起動
if __name__ == "__main__":
    app.run_server()