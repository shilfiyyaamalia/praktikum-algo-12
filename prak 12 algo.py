# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:43:02 2022

@author: Hp
"""

import pandas as pd

data = pd.read_csv("Negara.csv")

df = pd.DataFrame(data)
mean = df.groupby(["Benua"]).mean()
std = df.groupby(["Benua"]).std()

print(data)
print(mean)
print(std)