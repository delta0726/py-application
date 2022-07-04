# ******************************************************************************
# Course      : データ分析の基礎とインタラクティブダッシュボード作成入門
# Chapter     : 4 Matplotlibの基礎
# Theme       : 複数グラフの作成
# Creat Date  : 2022/07/04
# Final Update: //
# URL         : https://www.udemy.com/course/data-analysis_and_dashboard/
# ******************************************************************************


# ＜概要＞
# - 1つのプロットエリアに複数のプロットを記述する
#   --- ファセットではなく、個別のプロットを作成


# ＜目次＞
# 0 準備
# 1 サブプロットエリアの作成
# 2 サブプロットエリアの調整
# 3 サブプロットの作成


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import matplotlib.pyplot as plt
import numpy as np


# 1 サブプロットエリアの作成 ----------------------------------------------------

# プロット作成
# --- 2行2列のx番目にプロットを作成
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
fig.show()


# 2 サブプロットエリアの調整 ----------------------------------------------------

# プロット作成
# --- 前回のサブプロットのエリアを調整する
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig.show()


# 3 サブプロットの作成 ---------------------------------------------------------

# プロット作成
# --- 前回のサブプロットのエリアを調整する
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
plt.subplots_adjust(wspace=0.5, hspace=0.5)

# ax1
ax1.set_title('ax1')
x = [105, 210, 301, 440, 500]
y = [10, 20, 30, 50, 60]
ax1.plot(x, y)

# ax2
ax2.set_title('ax2')
x = ['A', 'B', 'C', 'D']
y = [400, 300, 150, 300]
ax2.bar(x, y)

# ax3
ax3.set_title('ax3')
x = np.random.randint(1, 101, 200)
y = np.random.randint(1, 101, 200)
ax3.scatter(x, y)

# ax4
ax4.set_title('ax4')
x = np.random.randint(1, 101, 200)
y = np.random.randint(1, 101, 200)
ax4.scatter(x, y)

plt.show()
