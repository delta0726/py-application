# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 8 Dashの標準コンポーネント
# Theme       : 3 Dash DataTable
# Topic       : 4 CSVファイルを用いたテーブル作成
# Update Date : 2022/3/27
# Page        : P175 - P176
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - データテーブルはデータ量が多くなると表示速度が遅くなる
#   --- virtualization引数をTrueにしてページを仮想化すると速度が改善する
#   --- あまり大量のデータを表示しないのがセオリー（どうせ見れない）


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch08_dash_standard_components\8-3-4_CSVファイルを用いたテーブル作成_2.py


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


# 1 レイアウトの作成 -----------------------------------------------------------

# ＜ポイント＞
# - virtualization引数をTrueにすることでテーブルを仮想化する
#   --- 表示速度の改善につながる


app.layout = html.Div(
    [
        dash_table.DataTable(
            page_size=700,
            virtualization=True,
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records")
        )
    ]
)


# 2 アプリの起動 ---------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
