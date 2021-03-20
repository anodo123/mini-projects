# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:21:11 2020

@author: DELL
"""
import pandas as pd
import numpy as np
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data",header = None)
y= df.loc[:,2:].values
print(y)