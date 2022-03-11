# ******************************************************************************
# Course      : Python/Streamlitによる機械学習WEBアプリの開発
# Chapter     : 4 実践2 Tipsの数値予測WEBアプリ
# Theme       : アプリ構築
# Creat Date  : 2022/3/11
# Final Update:
# URL         : https://www.udemy.com/course/pythonstreamlit/
# ******************************************************************************


# ＜実行：ターミナル＞
# conda activate pythonstreamlit
# streamlit run .\chap4_Tip_Prediction\tips_app.py


# ＜目次＞
# 0 準備
# 1 機械学習モデリング
# 2 アプリ構築


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly_express as px
from PIL import Image
from sklearn.linear_model import LinearRegression


# データ準備
data = sns.load_dataset('tips')


# 1 機械学習モデリング ------------------------------------------------------

# 特徴量のダミー変換
use_data = data[['total_bill', 'size', 'time', 'tip']]
use_data = pd.get_dummies(use_data, drop_first=True)

# 学習用データ
X = use_data[['total_bill', 'size', 'time_Dinner']]
y = use_data[['tip']]

# モデル構築
model = LinearRegression()
model.fit(X, y)


# 2 アプリ構築 ------------------------------------------------------------

# レイアウト設定
st.set_page_config(layout='wide')

# 画像挿入
image = Image.open('chap4_Tip_Prediction/picture/money.png')
st.image(image, caption='money')

# 分析データの表示
st.header('分析用データ')
st.write('データの件数は',str(len(data)),'件です')
st.write(use_data.astype('object'))

# サイドバーの設定
# --- 分析プロット用
st.sidebar.header('分析用プロット')
left_plot = st.sidebar.selectbox('箱ひげ図 [x軸]',["sex","smoker","time","day"])
right_plot = st.sidebar.selectbox('散布図 [x軸]',["total_bill","size"])

# 分析プロット
st.header('分析プロット')
st.write('y軸がチップの額になるプロットを作成します（左：ボックスプロット、右：散布図）')
col1, col2 = st.beta_columns(2)
with col1:
    fig = px.box(data, x=left_plot, y='tip')
    st.plotly_chart(fig)
with col2:
    fig = px.scatter(data, x=right_plot, y='tip')
    st.plotly_chart(fig)

# サイドバーの設定
# --- 機械学習用
st.sidebar.header('インプットデータ')
totalbill = st.sidebar.slider('Total bill', min_value = 0.0, max_value=50.0, step=0.5)
size = st.sidebar.slider('Size', min_value=1, max_value=10, step=1)
dinner = st.sidebar.radio('Lunch/Dinner', ['Lunch','Dinner'])
if dinner=='Lunch':
    dinner01 = 0
else:
    dinner01 = 1

# 入力値の表示
st.header('インプットデータの値')
st.write('Totalbill:', totalbill)
st.write('Size:', size)
st.write('Lunch or Dinner:', dinner)

# 入力値の整形
value_df = pd.DataFrame([], columns=['Totalbill', 'Size', 'Dinner flag'])
record = pd.Series([totalbill, size, dinner01], index=value_df.columns)
value_df = value_df.append(record, ignore_index=True)

# 予測
Y_pred = model.predict(value_df)

# 結果出力
st.header('チップの予測額')
st.write('チップ額はおそらく', str('{:.2g}'.format(Y_pred[0,0])), 'USドルくらいでしょう！')
