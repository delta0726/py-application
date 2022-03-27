# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 3 Dash DataTable
# Topic       : 5 テーブルの表示幅の変更と固定表示
# Update Date : 2022/3/27
# Page        : P176 - P178
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - テーブルを見やすくするためのオプション設定は無数にある
#   --- ヘッダー固定などが代表的


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-3-5_テーブルの表示幅の変更と固定表示_2.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_html_components as html
import dash_table
import pandas as pd

# データロード
fpath = "practice/ch08_dash_standard_components/data/kitakyushu_hinanjo.csv"
df = pd.read_csv(fpath, encoding="shift-jis")

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 ---------------------------------------------------------------

# ＜ポイント＞
# - ヘッダー固定などを追加


app.layout = html.Div(
    [
        dash_table.DataTable(
            style_cell={
                "textAlign": "center",
                "maxWidth": "80px",
                "minWidth": "80px",
                "whiteSpace": "normal",
            },
            fixed_rows={"headers": True},
            style_table={"minWidth": "100%"},
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records"),
        )
    ]
)


# 2 アプリの起動 --------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
