# ******************************************************************************
# Course      : データ分析の基礎とインタラクティブダッシュボード作成入門
# Chapter     : 3 Pandasの基礎
# Theme       : Seriesの操作
# Creat Date  : 2022/07/03
# Final Update: //
# URL         : https://www.udemy.com/course/data-analysis_and_dashboard/
# ******************************************************************************


# ＜概要＞
# - Pandas Seriesの基礎的な操作を復習する


# ＜目次＞
# 0 準備
# 1 Seriesの作成
# 2 Seriesの参照
# 3 Seriesの要素変更
# 4 Seriesの要素追加/削除


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import pandas as pd


# 1 Seriesの作成 -----------------------------------------------------------

# ＜ポイント＞
# - Seriesとはインデックス(ラベル)付けされた1次元のデータセット
#   --- Pandas DataFrameの列を構成する要素


# リストを変換
a_list = [7, 8, 9]
s1 = pd.Series(a_list)
print(s1)

# データ型を指定
a_list = [7, 8, 9]
s1 = pd.Series(a_list, dtype=float)
print(s1)

# 文字列から作成
a_arr = ['apple', 'banana', 'orange']
s2 = pd.Series(a_arr)
pd.Series(s2)

# インデックスを指定
# --- 要素数が同じ必要がある
val = [7, 8, 9]
name = ['apple', 'banana', 'orange']
s4 = pd.Series(val, index=name)
print(s4)

# 辞書型から作成
# --- 辞書のキーがインデックスとなる
a_dict = {'apple': 7, 'banana': 8, 'orange': 9}
s5 = pd.Series(a_dict)
print(s5)

# 辞書型から作成
# --- 辞書型にindex引数を指定すると、index引数の入力が優先される
# --- 今回は要素数が異なるのでcherryの値がNaNとなる
a_dict2 = {'apple': 7, 'banana': 8, 'orange': 9}
name = ['apple', 'banana', 'orange', 'cherry']
s6 = pd.Series(a_dict2, index=name)
print(s6)


# 2 Seriesの参照 ------------------------------------------------------------

# 準備：Seriesの作成
a_dict = {'apple': 7, 'banana': 8, 'orange': 9}
s5 = pd.Series(a_dict)
print(s5)

# インデックスを指定
s5['apple']

# インデックス番号を指定
s5[0]

# スライスを用いた指定
s5['apple':'orange']
s5[0:3]

# コンポーネントの取得
# --- 要素のみ取得
# --- インデックスのみ取得
s5.values
s5.index

# 条件抽出
# --- 要素ごとの条件適合の結果(True/False)の結果に応じて抽出
# --- Trueのみが取得される
s5[s5 > 7]
s5 > 7


# 3 Seriesの要素変更 ---------------------------------------------------------

# 準備：Seriesの作成
a_dict = {'apple': 7, 'banana': 8, 'orange': 9}
s5 = pd.Series(a_dict)
print(s5)

# 要素に変更値を代入
s5['apple'] = 100
print(s5)

# 複数要素をスライスで変更
s5[1:3] = 200
print(s5)


# 4 Seriesの要素追加/削除 --------------------------------------------------------

# 要素の追加
# --- appendによる追加はリタイア予定
a_list = [7, 8, 9]
b_list = [10, 11]
s7 = pd.Series(a_list)
s8 = pd.Series(b_list)
s7.append(s8, ignore_index=True)
pd.concat([s7, s8], ignore_index=True)

# 要素の削除
# --- 元のオブジェクトを維持する
# --- 削除したオブジェクトは別の変数に定義
a_dict = {'apple': 7, 'banana': 8, 'orange': 9}
s9 = pd.Series(a_dict)
s10 = s9.drop(index='banana')
print(s10)
print(s9)

# 要素の削除
# --- 元のオブジェクト自体を変更する
# --- s10はNoneとなっている点に注意
a_dict = {'apple': 7, 'banana': 8, 'orange': 9}
s9 = pd.Series(a_dict)
s10 = s9.drop(index='banana', inplace=True)
print(s10)
print(s9)
