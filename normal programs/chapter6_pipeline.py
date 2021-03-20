# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:35:34 2020

@author: DELL
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data",header = None)
x = df.loc[:,2:].values
y= df.loc[:,1].values
le = LabelEncoder()
y = le.fit_transform(y)
le.transform(['M','B'])
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size = 0.20,random_state=1)
pipe_lr = Pipeline([('scl',StandardScaler()),('pca',PCA(n_components=2)),('clf',LogisticRegression(random_state=1))])
pipe_lr.fit(X_train,Y_train)
print("Test Accuracy:%.3f"%pipe_lr.score(X_test,Y_test))