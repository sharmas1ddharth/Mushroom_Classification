import pandas as pd
from src import mushroom_classification

"""
data = pd.read_csv('data/raw/mushrooms.csv')
cols = list(data.columns)

for col in cols:
    unique_val = data[col].unique()
    print(f"{col} = {unique_val}")






Process finished with exit code 0

"""

# data = pd.read_csv("C:\\Users\\Siddharth\\Desktop\\Github Projects\\Mushroom_Classification\\data\\processed\\X_train.csv")
# #print(data.dtypes)
# cap_shape = {0: 'convex', 5: 'bell', 2: 'sunken', 3: 'flat', 4: 'knobbed',
#              1: 'conical'}  # ['x', 'b', 's', 'f', 'k', 'c']

# for key, val in cap_shape.items():
#     print(key)

from flask import request


