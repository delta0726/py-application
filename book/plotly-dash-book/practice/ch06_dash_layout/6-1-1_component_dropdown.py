# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 1-1 コンポーネントの作成
# Creat Date  : 2022/3/20
# Final Update:
# Page        : P104 - P105
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - DashのUIの部品となるウィジェットを確認する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-1-1_dash_component_dropdown.py


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# レイアウト
import dash
import dash_core_components as dcc

# インスタンス生成
app = dash.Dash(__name__)


# 1 コンポーネントの作成 --------------------------------------------------------

# ドロップダウンの要素
item_dropdown = [
    {"label": "赤", "value": "red"},
    {"label": "黄", "value": "yellow"},
    {"label": "青", "value": "blue"}
]

app.layout = dcc.Dropdown(options=item_dropdown,
                          value="red",
                          clearable=False,
                          style={"textAlign": "center"})

# 2 アプリ起動 ----------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
