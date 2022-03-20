# ******************************************************************************
# Book        : Pythonインタラクティブデータビジュアライゼーション入門
# Chapter     : 6 Dashレイアウト
# Theme       : 1 コンポーネント
# Topic       : 2 コンポーネントの主要な属性
# Update Date : 2022/3/20
# Page        : P106 - P107
# URL         : https://github.com/plotly-dash-book/plotly-dash-book
# ******************************************************************************


# ＜概要＞
# - 各コンポーネントで共通して用いられる属性(プロパティ)を確認する


# ＜主要な属性＞
# - Children  : Divクラスでリストに格納した複数コンポーネントを指定
# - id        : コンポーネントの名前（コールバックで使用）
# - className : HTMLのclassグローバル属性 （Pythonのクラスとは異なる）
# - options   : Dropdownなどのウィジェットの要素を指定
# - style     : スタイル設定（辞書にCSSを格納して渡す）
# - value     : コンポーネントの値


# ＜ヘルプ確認＞
# dcc.Dropdownにカーソールをあてる

import dash
import dash_core_components as dcc

dcc.Dropdown(options=[],
             value="red",
             clearable=False,
             style={"textAlign": "center"})
