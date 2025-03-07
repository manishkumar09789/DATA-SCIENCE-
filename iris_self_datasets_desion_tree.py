# -*- coding: utf-8 -*-
"""IRIS.SELF.DATASETS.Desion.tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Jn9LBoMpw1WHI9yRSxBBlTuaQ3b_M4H
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris=load_iris()
iris

iris.data

iris.target

df=sns.load_dataset("iris")

df.head()

x=df.iloc[:,:-1]
y=iris.target
x,y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print(x_train)

treemodel=DecisionTreeClassifier()
treemodel.fit(x_train,y_train)

from sklearn import tree
plt.figure(figsize=(10,10))
tree.plot_tree(treemodel,filled=True,fontsize=10)
plt.show()