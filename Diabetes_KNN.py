# -*- coding: utf-8 -*-
"""Diabetes,KNN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19NcUmqNckJjCvrDUY216Ag00V1HvCMSE
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv("/content/diabetes.csv")
df

x = df[['Pregnancies', 'Glucose', 'BloodPressure','Age']].values
y=df['Outcome'].values
print(x)
print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

df=np.array([[1,85,66,29]])
y_pred=knn.predict(df)
print(y_pred)

