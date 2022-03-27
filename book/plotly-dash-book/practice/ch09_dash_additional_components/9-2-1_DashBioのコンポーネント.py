# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 9 Dashの追加コンポーネント
# Theme       : 2 Dash Bio
# Topic       : 1 DashBioのコンポーネント
# Update Date : 2022/3/27
# Page        : P192 - P194
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - DashBioはバイオインフォマティクスで使用するオブジェクトをサポートしている
#   --- ここではirisデータセットでクラスタグラムを作成する


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch09_dash_additional_components\9-2-1_DashBioのコンポーネント.py


# ＜目次＞
# 0 準備
# 1 レイアウトの作成
# 2 アプリの起動


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
import plotly

# データロード
iris = plotly.data.iris()
iris = iris.drop("species", 1)

# インスタンス生成
app = dash.Dash(__name__)


# 1 レイアウトの作成 -------------------------------------------------------------

app.layout = html.Div(
    [
        dcc.Graph(
            figure=dashbio.Clustergram(
                data=iris.values,
                column_labels=list(iris.columns.values),
                width=800,
                height=800,
                # ヒートマップの配色
                color_map=[[0.0, "white"], [0.5, "gray"], [1.0, "black"]],
                # デントログラムの高さの設定（行側、列側、ヒートマップ比）
                display_ratio=[0.3, 0.1]
            )
        )
    ]
)


# 2 アプリの起動 -------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
