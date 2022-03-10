# ******************************************************************************
# Course      : Python/Streamlitによる機械学習WEBアプリの開発
# Chapter     : 2 Streamlit入門
# Theme       : 各種ウィジェットの追加
# Creat Date  : 2022/3/11
# Final Update:
# URL         : https://www.udemy.com/course/pythonstreamlit/
# ******************************************************************************


# ＜ポイント＞
# - streamlitはサイドバーとメイン画面に分けて構成される
# - 文字やプロットやテーブルなど各種オブジェクトを挿入することができる


# ＜実行：ターミナル＞
# conda activate pythonstreamlit
# streamlit run .\chap2_Introduction\2_add_widgets.py


# ＜停止：ターミナル＞
# Ctrl + C


# ライブラリ
import streamlit as st
import seaborn as sns
import plotly.express as px


# ページレイアウト
st.set_page_config(layout='wide')

# タイトル
st.title('タイトル')

# 文字の挿入
st.header('header')
st.write('write')

# 文字の挿入
# --- マークダウン記法
st.write('# markdown_level-1')
st.write('## markdown_level-2')
st.write('### markdown_level-3')

# データフレームの挿入
# --- データをオブジェクト型に変換する必要がある
data = sns.load_dataset('tips')
st.write(data.astype('object'))

# グラフの挿入
fig = px.scatter(data, x='total_bill', y='tip')
st.plotly_chart(fig)

# ウィジェット
favrorite = st.selectbox('セレクトボックスです！', ['apple', 'orange', 'grape'])
st.slider('スライダーです！', min_value=0, max_value=100, step=5)
st.radio('ラジオボタンです！', ['apple', 'orange'])

# ウィジェットの値を受け取る
st.write('好きな食べ物は何ですか？：', favrorite)

# サイドバーの作成
st.sidebar.header('ヘッダー')
st.sidebar.write('write1')
st.sidebar.selectbox('セレクトボックスです！', ['apple', 'orange', 'grape'], key='test1')
st.sidebar.slider('スライダーです！', min_value=0, max_value=100, step=5, key='test2')
st.sidebar.radio('ラジオボタンです！', ['apple', 'orange'], key='test3')
