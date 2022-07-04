# ******************************************************************************
# Course      : データ分析の基礎とインタラクティブダッシュボード作成入門
# Chapter     : 5 Streamlitの基礎
# Theme       : マジックコマンドの使用
# Creat Date  : 2022/07/05
# Final Update: //
# URL         : https://www.udemy.com/course/data-analysis_and_dashboard/
# ******************************************************************************


# ＜概要＞
# - Streamlitはマジックコマンドとして使用可能な記法が複数ある


# ＜実行：ターミナル＞
# conda activate data-analysis_and_dashboard
# streamlit run .\sec5_streamlit\5-2_magic_comamnd.py


# ＜目次＞
# 0 準備
# 1 文字列の表示
# 2 データフレームの表示
# 3 文字列の表示


# 0 準備 ------------------------------------------------------------

# ライブラリ
import streamlit as st


# 1 データフレームの表示 -----------------------------------------------

# データフレーム作成
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [40, 30, 20, 10]
})

# 表示
#st.write(df)
df


# 2 オブジェクトの表示 ------------------------------------------------

# 数字
x = 100
x


df_column = df.columns
df_column


# 3 文字列の表示 -----------------------------------------------------

"""
# マジックコマンドを使ってみる
文字列の入力
"""


"""
```
import streamlit as st
print('Hello Streamlit')
```
"""
