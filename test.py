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

data = pd.read_csv("C:\\Users\\Siddharth\\Desktop\\Github Projects\\Mushroom_Classification\\data\\processed\\X_train.csv")
print(data.dtypes)