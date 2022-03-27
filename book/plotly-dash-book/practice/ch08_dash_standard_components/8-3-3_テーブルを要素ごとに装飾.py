# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 3 Dash DataTable
# Topic       : 3 テーブルを要素ごとに装飾
# Update Date : 2022/3/27
# Page        : P173 - P175
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - テーブル要素をif文を組み合わせてスタイル定義することが可能


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-3-3_テーブルを要素ごとに装飾.py


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
# - データフレームのスタイルは辞書で渡す
#   --- if文などの条件も辞書で渡す（複雑になりがち）


app.layout = dash_table.DataTable(
    fill_width=False,
    columns=[
        {"name": "number", "id": "number"},
        {"name": "area", "id": "area"},
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
    # 列全体のスタイル
    # --- 条件は辞書で渡す
    style_cell_conditional=[
        {"if": {"column_id": "number"}, "fontSize": 24, "backgroundColor": "#FFEEE4"}
    ],
    # ヘッダーのスタイル
    style_header_conditional=[
        {"if": {"column_id": "area"}, "textAlign": "center", "width": 150},
        {"if": {"column_id": "tsuyu-iri"}, "backgroundColor": "#FBFFB9"},
    ],
    # データ部分のスタイル
    style_data_conditional=[
        {"if": {"row_index": "odd"}, "backgroundColor": "#FBFFB9"},
        {"if": {"column_id": "tsuyu-iri", "filter_query": "{number} > 3"}, "backgroundColor": "#41D3BD"},
    ],
)


# 2 アプリの起動 -------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
