# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 3 Dash DataTable
# Topic       : 1 テーブル作成
# Update Date : 2022/3/27
# Page        : P171 - P173
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - dash_tableクラスを用いるとインタラクティブなデータテーブルを作成することができる
#   --- テーブルは編集や保存も可能


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-3-1_テーブル作成.py


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


# 1 レイアウトの作成 -----------------------------------------------------------

app.layout = dash_table.DataTable(
    # コラム定義
    columns=[
        {"name": "number", "id": "number"},
        {"name": "region", "id": "area"},
        {"name": "tsuyu-iri", "id": "tsuyu-iri"},
    ],
    # データ定義
    # --- 1レコードずつ辞書型で定義
    data=[
        {"number": 0, "area": "okinawa", "tsuyu-iri": "5/16"},
        {"number": 1, "area": "kyusyu-south", "tsuyu-iri": "5/31"},
        {"number": 2, "area": "kyusyu-north", "tsuyu-iri": "6/26"},
        {"number": 3, "area": "shikoku", "tsuyu-iri": "6/26"},
        {"number": 4, "area": "chugoku", "tsuyu-iri": "6/26"},
        {"number": 5, "area": "kinki", "tsuyu-iri": "6/26"},
    ],
    fill_width=False,
)


# 2 アプリの起動 ---------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
