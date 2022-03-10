# ******************************************************************************
# Course      : Python/Streamlitによる機械学習WEBアプリの開発
# Chapter     : 3 実践1 iris分類予測アプリの作成
# Theme       : アプリ構築
# Creat Date  : 2022/3/11
# Final Update:
# URL         : https://www.udemy.com/course/pythonstreamlit/
# ******************************************************************************


# ＜概要＞
# - irisのSpeciesをロジスティック回帰モデルで判別するモデルを作成する
# - モデルをstreamlitのWebアプリとして実装する


# ＜実行：ターミナル＞
# conda activate pythonstreamlit
# streamlit run .\chap3_iris_kmeans\iris_app.py


# ＜目次＞
# 0 準備
# 1 モデリング
# 2 アプリ構築


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


# データロード
iris = load_iris()

# モデル用のデータ
X = iris.data[:, [0, 2]]
y = iris.target


# 1 モデリング ------------------------------------------------------------

# モデル構築
clf = LogisticRegression()
clf.fit(X, y)


# 2 アプリ構築 -----------------------------------------------------------

# サイドバー
st.sidebar.header('Input Features')
sepalValue = st.sidebar.slider('sepal length [cm]', min_value=0.0, max_value=10.0, step=0.1)
petalValue = st.sidebar.slider('petal length [cm]', min_value=0.0, max_value=10.0, step=0.1)

# sepalValue = 4.5
# petalValue = 6.5

# データ作成
value_df = pd.DataFrame([], columns=['data', 'sepal_length', 'petal_length'])
record = pd.Series(['data', sepalValue, petalValue], index=value_df.columns)
value_df = value_df.append(record, ignore_index=True)
value_df.set_index('data', inplace=True)

# 予測
pred_probs = clf.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs,
                       columns=['setosa', 'versicolor', 'virginica'],
                       index=['probability'])

# メインパネル
st.title('Iris Classifier')
st.write('## Input Value')
st.write(value_df)

st.write('## Output Probability')
st.write(pred_df)

st.write('## Result')
name = pred_df.idxmax(axis=1).tolist()
st.write('このIrisはきっと', str(name[0]), "です！")
