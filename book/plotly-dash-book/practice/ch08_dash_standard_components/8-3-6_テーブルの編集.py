# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 3 Dash DataTable
# Topic       : 6 テーブルの編集
# Update Date : 2022/3/27
# Page        : P178 - P180
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - データテーブルを様々な観点で編集可能にすることができる
#   --- 引数で個別にコントロール
#   --- モデルの複雑な条件設定などをテーブル化して管理することでインターフェースの簡素化が可能となる


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-3-6_テーブルの編集.py


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


# 1 レイアウトの作成 ------------------------------------------------------------

app.layout = html.Div(
    [
        dash_table.DataTable(
            style_cell={
                "textAlign": "center",
                "maxWidth": "80px",
                "whiteSpace": "normal",
                "minWidth": "80px",
            },
            fixed_rows={"headers": True, "data": 0},
            style_table={"maxHeight": 800, "maxWidth": "100%"},
            # セルの編集を可能にする
            editable=True,
            # 列のフィルタリングを可能にする
            filter_action="native",
            # 行の消去を可能にする
            row_deletable=True,
            # 複数行の選択を可能にする
            row_selectable="multi",
            # 列のソートを可能にする
            sort_action="native",
            # ソートを複数列を条件で可能にする
            sort_mode="multi",
            columns=[
                {"name": col, "id": col, "deletable": True, "selectable": True}
                for col in df.columns
            ],
            data=df.to_dict("records"),
            page_size=10,
            export_format="csv",
        )
    ]
)


# 2 アプリの起動 ------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
