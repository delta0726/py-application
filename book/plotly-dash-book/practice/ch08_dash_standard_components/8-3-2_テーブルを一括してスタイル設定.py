# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 3 Dash DataTable
# Topic       : 2 テーブルを一括してスタイル設定
# Update Date : 2022/3/27
# Page        : P173
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - DataTableコンポーネントはテーブル全体からセル単位まで詳細にスタイル設定が可能


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-3-2_テーブルを一括してスタイル設定.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_table

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 ------------------------------------------------------------

# ＜ポイント＞
# - データテーブルについても各種スタイル設定をすることができる


app.layout = dash_table.DataTable(
    fill_width=False,
    columns=[
        {"name": "number", "id": "number"},
        {"name": "region", "id": "area"},
        {"name": "tsuyu-iri", "id": "tsuyu-iri"},
    ],
    data=[
        {"number": 0, "area": "okinawa", "tsuyu-iri": "5/16"},
        {"number": 1, "area": "kyusyu-south", "tsuyu-iri": "5/31"},
        {"number": 2, "area": "kyusyu-north", "tsuyu-iri": "6/26"},
        {"number": 3, "area": "shikoku", "tsuyu-iri": "6/26"},
        {"number": 4, "area": "chugoku", "tsuyu-iri": "6/26"},
        {"number": 5, "area": "kinki", "tsuyu-iri": "6/26"},
    ],
    style_cell={"width": 160, "fontSize": 24, "textAlign": "center"},
)


# 2 アプリの起動 -----------------------------------------------------------------

app.run_server(debug=True)
