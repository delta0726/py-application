# ******************************************************************************
# Course      : データ分析の基礎とインタラクティブダッシュボード作成入門
# Chapter     : 5 Streamlitの基礎
# Theme       : はじめてのstreamlit
# Creat Date  : 2022/07/05
# Final Update: //
# URL         : https://www.udemy.com/course/data-analysis_and_dashboard/
# ******************************************************************************


# ＜概要＞
# - Streamlitを使ってみる


# ＜実行：ターミナル＞
# conda activate data-analysis_and_dashboard
# streamlit run .\sec5_streamlit\5-1_first-streamlit.py


# ＜目次＞
# 0 準備
# 1 文字列の表示
# 2 データフレームの表示


# 0 準備 ------------------------------------------------------------

# ライブラリ
import streamlit as st
import pandas as pd


# 1 文字列の表示 -----------------------------------------------------

# コンポーネント表示
st.title('タイトル表示')
st.header('ヘッダー表示')
st.subheader('サブヘッダー表示')
st.text('テキスト表示')


# 2 データフレームの表示 -----------------------------------------------

# データフレーム作成
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [40, 30, 20, 10]
})

# 表示
# --- テーブル上でソートなどの操作が可能
st.write(df)

# 表示
# --- 引数を指定してデータフレームのコントロールが可能
st.dataframe(df)
st.dataframe(df, width=200, height=200)
st.dataframe(df.style.highlight_max(axis=0))

# 固定テーブル
st.table(df)