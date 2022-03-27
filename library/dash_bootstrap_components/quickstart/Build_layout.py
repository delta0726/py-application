# ******************************************************************************
# Library     : Dash Bootstrap Components
# Category    : Quick Start
# Theme       : Build the layout
# Update Date : 2022/3/28
# URL         : https://dash-bootstrap-components.opensource.faculty.ai/examples/iris/
# ******************************************************************************


# ＜概要＞
# - レイアウトのみの最小限のアプリ


# ＜実行＞
# conda activate dash_bootstrap_components
# python .\quickstart\Build_layout.py



# 実行例 ---------------------------------------------------------------------------------

# ライブラリ
import dash
import dash_bootstrap_components as dbc

# インスタンス生成
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# レイアウト作成
# --- アラートに文字表示
app.layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)

# アプリ起動
if __name__ == "__main__":
    app.run_server()
