# ******************************************************************************
# Course      : データ分析の基礎とインタラクティブダッシュボード作成入門
# Chapter     : 4 Matplotlibの基礎
# Theme       : 簡単なグラフの作成
# Creat Date  : 2022/07/04
# Final Update: //
# URL         : https://www.udemy.com/course/data-analysis_and_dashboard/
# ******************************************************************************


# ＜概要＞
# - Pandas Seriesの基礎的な操作を復習する


# ＜目次＞
# 0 準備
# 1 はじめてのプロット作成
# 2 棒グラフの作成
# 3 ヒストグラムの作成
# 4 散布図の作成


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import matplotlib.pyplot as plt
import numpy as np


# 1 はじめてのプロット作成 ------------------------------------------------------

# データ定義
x = [105, 210, 301, 440, 500]
y = [10, 20, 30, 50, 60]

# プロット作成
fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
ax.plot(x, y, marker='o', color='red', linestyle='--', linewidth=2)
ax.set_title('practice matplotlib')
ax.set_xlabel('x')
ax.set_xlabel('y')
ax.grid()
plt.show()


# 2 棒グラフの作成 ----------------------------------------------------------

# データ定義
x = ['A', 'B', 'C', 'D']
y = [400, 300, 150, 300]

# プロット作成
fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
ax.bar(x, y)
plt.show()


# 3 ヒストグラムの作成 ------------------------------------------------------

# データ定義
x = np.random.randn(1000)

# プロット作成
fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
ax.hist(x, bins=50)
plt.show()


# 4 散布図の作成 ----------------------------------------------------------

# データ定義
x = np.random.randint(1, 101, 200)
y = np.random.randint(1, 101, 200)

# プロット作成
fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
ax.scatter(x, y)
plt.show()
