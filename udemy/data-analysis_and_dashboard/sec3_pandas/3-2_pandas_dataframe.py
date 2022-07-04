# ******************************************************************************
# Course      : データ分析の基礎とインタラクティブダッシュボード作成入門
# Chapter     : 3 Pandasの基礎
# Theme       : DataFrameの操作
# Creat Date  : 2022/07/04
# Final Update: //
# URL         : https://www.udemy.com/course/data-analysis_and_dashboard/
# ******************************************************************************


# ＜概要＞
# - Pandas DataFrameの基礎的な操作を復習する


# ＜目次＞
# 0 準備
# 1 DataFrameの作成
# 2 DataFrameの参照
# 3 名前による要素抽出(loc)
# 4 番号による要素抽出(iloc)
# 5 条件によるデータ抽出
# 6 データの変更/追加
# 7 データの削除


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import pandas as pd


# 1 DataFrameの作成 ----------------------------------------------------------

# ＜ポイント＞
# - DataFrameとはインデックス(ラベル)を持つ二次元のデータ構造
#   --- Pandas Seriesが列を構成している


# 二次元配列の作成
# --- リストの中にリストが入っている
val = [[1, 2, 3], [4, 5, 6]]

# データフレームの作成
df = pd.DataFrame(val, dtype=float)
print(df)

# データ型の確認
df.dtypes

# データフレームの作成
# --- 行名と列名を追加
val = [[1, 2, 3], [4, 5, 6]]
df = pd.DataFrame(val, dtype=float, index=['r0', 'r1'], columns=['c0', 'c1', 'c2'])
print(df)

# データフレームの作成
# --- Pandas Seriesから辞書を定義して作成
sr_age = pd.Series([23, 31, 49, 60])
sr_gender = pd.Series(['M', 'F', 'F', 'M'])
sr_height = pd.Series([175, 160, 156, 180])
sr_weight = pd.Series([65, 40, 48, 85])
df_info = pd.DataFrame({
    'age': sr_age,
    'gender': sr_gender,
    'height': sr_height,
    'weight': sr_weight
})
print(df_info)

# データフレームの作成
# --- Pandas Seriesに予めインデックスを持たせる
# --- 要素を持たない箇所はNaNとなる
sr_age = pd.Series([23, 31, 49, 60], index=['sato', 'yamada', 'suzuki', 'tanaka'])
sr_gender = pd.Series(['M', 'F', 'M'], index=['sato', 'yamada', 'suzuki'])
sr_height = pd.Series([160, 156, 180], index=['yamada', 'suzuki', 'tanaka'])
sr_weight = pd.Series([65, 85], index=['sato', 'tanaka'])
df_info = pd.DataFrame({
    'age': sr_age,
    'gender': sr_gender,
    'height': sr_height,
    'weight': sr_weight
})
print(df_info)


# 2 DataFrameの参照 ----------------------------------------------------------

# 準備：データフレームの作成
sr_age = pd.Series([23, 31, 49, 60], index=['sato', 'yamada', 'suzuki', 'tanaka'])
sr_gender = pd.Series(['M', 'F', 'M'], index=['sato', 'yamada', 'suzuki'])
sr_height = pd.Series([160, 156, 180], index=['yamada', 'suzuki', 'tanaka'])
sr_weight = pd.Series([65, 85], index=['sato', 'tanaka'])
df_info = pd.DataFrame({
    'age': sr_age,
    'gender': sr_gender,
    'height': sr_height,
    'weight': sr_weight
})
print(df_info)

# データフレームの概要
df_info.info()

# データフレームの行列数
df_info.shape
df_info.shape[0]
df_info.shape[1]

# データフレームの全要素数
df_info.size

# データ確認
df_info.head(2)
df_info.tail(2)


# 3 名前による要素抽出(loc) ----------------------------------------------------

# 特定列の抽出
# --- Pandas Series
# --- Pandas DataFrame
df_info['age']
df_info[['age']]

# 複数列の抽出
df_info[['age', 'gender']]

# locによる抽出
# --- 行の抽出
# --- 列の抽出
# --- 要素の抽出
df_info.loc['suzuki']
df_info.loc[:, 'age']
df_info.loc['suzuki', 'height']


# 4 番号による要素抽出(iloc) ---------------------------------------------------

# データ確認
print(df_info)

# ilocによる抽出
df_info.iloc[0, 0]
df_info.iloc[1, 2]
df_info.iloc[1:4, 2]
df_info.iloc[1, :]


# 5 条件によるデータ抽出 -----------------------------------------------------

# 身長の条件で抽出
df_info[df_info['height'] > 170]

# 性別の条件で抽出
df_info[df_info['gender'] == 'M']


# 6 データの変更/追加 ---------------------------------------------------------------

# 準備：データフレームの作成
sr_age = pd.Series([23, 31, 49, 60], index=['sato', 'yamada', 'suzuki', 'tanaka'])
sr_gender = pd.Series(['M', 'F', 'M'], index=['sato', 'yamada', 'suzuki'])
sr_height = pd.Series([160, 156, 180], index=['yamada', 'suzuki', 'tanaka'])
sr_weight = pd.Series([65, 85], index=['sato', 'tanaka'])
df_info = pd.DataFrame({
    'age': sr_age,
    'gender': sr_gender,
    'height': sr_height,
    'weight': sr_weight
})
print(df_info)

# 列の変更
df_info['height'] = 175
print(df_info)

# 値の変更（名前指定）
df_info.loc['sato', 'weight'] = 100
print(df_info)

# 値の変更（番号指定）
df_info.iloc[0] = 30
print(df_info)

# 新しい列の追加
df_info['new_column'] = 1
df_info.loc['new_index'] = 0
df_info


# 7 データの削除 -----------------------------------------------------------------

# 準備：データフレームの作成
sr_age = pd.Series([23, 31, 49, 60], index=['sato', 'yamada', 'suzuki', 'tanaka'])
sr_gender = pd.Series(['M', 'F', 'M'], index=['sato', 'yamada', 'suzuki'])
sr_height = pd.Series([160, 156, 180], index=['yamada', 'suzuki', 'tanaka'])
sr_weight = pd.Series([65, 85], index=['sato', 'tanaka'])
df_info = pd.DataFrame({
    'age': sr_age,
    'gender': sr_gender,
    'height': sr_height,
    'weight': sr_weight
})
print(df_info)

# 列の削除
# --- 元のデータは変更されていない（別変数を定義していない）
df_info.drop(labels='age', axis=1)
print(df_info)

# 列の削除
# --- 元のデータ自体を変更している
df_info.drop(labels='age', axis=1, inplace=True)
print(df_info)

# 行の削除
# --- 元のデータは変更されていない（別変数を定義していない）
df_info.drop(labels=['suzuki', 'tanaka'], axis=0)
print(df_info)

# 行の削除
# --- 元のデータ自体を変更している
df_info.drop(labels=['suzuki', 'tanaka'], axis=0, inplace=True)
print(df_info)
