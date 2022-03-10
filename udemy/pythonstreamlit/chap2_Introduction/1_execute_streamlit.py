# ******************************************************************************
# Course      : Python/Streamlitによる機械学習WEBアプリの開発
# Chapter     : 2 Streamlit入門
# Theme       : Streamlitの実行
# Creat Date  : 2022/3/10
# Final Update:
# URL         : https://www.udemy.com/course/pythonstreamlit/
# ******************************************************************************


# ＜ポイント＞
# - streamlitは｢.py｣ファイルで作成する（ファイル名には制約がない）
# - ターミナルから起動する


# ＜実行：ターミナル＞
# conda activate pythonstreamlit
# streamlit run .\chap2_Introduction\2_add_widgets.py


# ＜停止：ターミナル＞
# Ctrl + C


# ライブラリ
import streamlit as st

# ページレイアウト
st.set_page_config(layout='wide')

# タイトル
st.title('タイトル')