import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('insurance.csv')
print(df.head())
print("\n")
print(df.shape)
print("\n")
print(df.info())
print("\n")
print(df.describe())
print("\n")
print(df.isnull().sum())
print("\n")
print(df.columns)
print("\n")
numeric_columns = ['age','bmi', 'children','charges']
# for col in numeric_columns:
#     plt.figure(figsize=(6,4))
#     sns.histplot(df[col],kde=True,bins = 20)
#     plt.title(f'Distribution of {col}')
#     plt.show()
sns.countplot(x=df['children'])
plt.show()