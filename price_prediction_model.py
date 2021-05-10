import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
df1 = pd.read_csv("bengaluru_house_prices.csv")
df1.head()


df2 = df1.drop(["availability","area_type",'society','balcony'],axis = 'columns')
df3=df2.dropna()

df3['bhk'] = df3['size'].apply(lambda x: x.split(' ')[0])
