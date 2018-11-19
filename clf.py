#!/usr/bin/env python3
import numpy as np
import pandas as pd
import xgboost
from sklearn import tree
from xgboost import XGBClassifier

df = pd.read_csv('./data.csv', sep=',')

data = np.array(df)[:, 1: -1]
label = np.array(df)[:, -1]

data[:, 0] = [['Male', 'Female'].index(i) for i in data[:, 0]]
data[:, 3] = [['auto', 'non-auto'].index(i) for i in data[:, 3]]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(list(data), list(label))
# with open('clf.txt', 'w') as f:
#     f = tree.export_graphviz(clf, out_file=f)

clf2 = XGBClassifier(n_estimators = 1)
clf2.fit(data, label)
tree = clf2.get_booster().get_dump()
for i in tree:
    print(i)
