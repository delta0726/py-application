# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 2 スタイル設定
# Topic       : 3 外部CSSを用いたスタイル設定
# Update Date : 2022/3/21
# Page        : P110 - P112
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - 外部CSSを読込むことでレイアウトを一括指定することが可能
# - DashでもデフォルトCSSが利用されている（外部CSSを指定しない場合に適用される）


# ＜実行＞
# conda activate plotly-dash-book
# python .\practice\ch06_dash_layout\6-2-3_style_external_css.py


# ＜目次＞
# 0 準備
# 1 コンポーネントの作成
# 2 アプリ起動


# 0 準備 ---------------------------------------------------------------------

# ＜ポイント＞
# - インスタンス生成時に外部CSSのURLリンクを渡す
#   --- 当該アプリで使用するコンポーネント全てに適用される

# ライブラリ
import dash
import dash_core_components as dcc
import dash_html_components as html

# フラグ設定
# --- True: スタイルあり  False: スタイルなし
flg_style = True

# インスタンス生成
# --- 外部スタイルシートの読み込み
if flg_style:
    external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
else:
    app = dash.Dash(__name__)


# 1 コンポーネントの作成 ---------------------------------------------------------

# ＜ポイント＞
# - Dashのデフォルトでは縦並びだが、外部CSSが適用されると横並びとなる


# レイアウト設定
# --- 複数コンポーネントを追加
app.layout = html.Div(
    [
        html.H1("スタイル", className="three columns"),
        dcc.Input(placeholder="スタイルシートテスト", className="three columns"),
        dcc.Graph(className="six columns"),
    ]
)


# 2 アプリ起動 ------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(debug=True)
