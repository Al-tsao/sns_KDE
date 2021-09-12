#Standard

import numpy as np

import pandas as pd

from numpy.random import randn

from pandas import Series, DataFrame

#Stats

from scipy import stats

#Matplotlib

import matplotlib as mpl

import matplotlib.pyplot as plt

#Seaborn

import seaborn as sns

#Draw

sns.set() #設定繪圖改為seaborn繪製

s = Series(randn(100))

sns.kdeplot(s, color='r', linewidth=5, label='aaaa') #color:制定bar的顏色；linewidth: 邊線粗細；label: 顯示圖表，要搭配legend()使用
plt.xlabel('this is x')

plt.ylabel('this is y')

plt.title('this is a demo')

plt.legend()

plt.show() #繪圖