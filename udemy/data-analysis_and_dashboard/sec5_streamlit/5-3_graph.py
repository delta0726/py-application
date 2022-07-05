# ******************************************************************************
# Course      : データ分析の基礎とインタラクティブダッシュボード作成入門
# Chapter     : 5 Streamlitの基礎
# Theme       : 3 グラフの挿入
# Creat Date  : 2022/07/05
# Final Update: //
# URL         : https://www.udemy.com/course/data-analysis_and_dashboard/
# ******************************************************************************


# ＜概要＞
# - Streamlitはマジックコマンドとして使用可能な記法が複数ある


# ＜実行：ターミナル＞
# conda activate data-analysis_and_dashboard
# streamlit run .\sec5_streamlit\5-3_graph.py


# ＜目次＞
# 0 準備
# 1 データフレームの表示
# 2 streamlitのグラフ機能を使用
# 3 外部ライブラリのグラフを埋め込み
# 4 地図グラフの表示
# 5 3次元マップの表示


# 0 準備 ------------------------------------------------------------

# ライブラリ
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk


# 1 データフレームの表示 -----------------------------------------------

# データフレーム作成
df = pd.DataFrame(np.random.randn(20, 3),
                  columns=['a', 'b', 'c'])

df


# 2 streamlitのグラフ機能を使用 ----------------------------------------

# ラインチャート
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)


# 3 外部ライブラリのグラフを埋め込み ---------------------------------------

# エリア定義
fig = plt.figure(figsize=(10, 5))
ax = plt.axes()

# データ作成
x = [105, 210, 301, 440, 500]
y = [10, 20, 30, 40, 50]

# プロット作成
ax.plot(x, y)
st.pyplot(fig)


# 4 地図グラフの表示 -------------------------------------------------------

# 東京の緯度/経度
tokyo_lat = 35.69
tokyo_lon = 139.69

# ダミーデータの作成
df_tokyo = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [tokyo_lat, tokyo_lon],
    columns=['lat', 'lon']
)

# 地図プロット
st.map(df_tokyo)


# 5 3次元マップの表示 -------------------------------------------------------

# 東京の緯度/経度
tokyo_lat = 35.69
tokyo_lon = 139.69

# ダミーデータの作成
df_tokyo = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [tokyo_lat, tokyo_lon],
    columns=['lat', 'lon']
)

# ビューの設定
view = pdk.ViewState(latitude=tokyo_lat, longitude=tokyo_lon, pitch=50, zoom=11)

# レイアー設定
hexagon_layer = pdk.Layer('HexagonLayer',
                          data=df_tokyo,
                          get_position=['lon', 'lat'],
                          elevation_scale=6,
                          radius=200,
                          extruded=True)

# プロット表示
layer_map = pdk.Deck(layers=hexagon_layer, initial_view_state=view)
st.pydeck_chart(layer_map)
