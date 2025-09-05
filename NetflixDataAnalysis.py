import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

df=pd.read_csv('mymoviedb.csv',lineterminator='\n',encoding='utf-8')
# print(df)
# print(df.head())
# df.info()

print(df['Genre'].head())
print(df.duplicated().sum())

print(df.describe()) 

# All date format to Seprate Year Only
df['Release_Date']=pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtype)

#Only Year show code=
df['Release_Date']=df['Release_Date'].dt.year
print(df['Release_Date'].dtype)  #check dataType
print(df['Release_Date'].head())


# Droping the columns
cols =['Overview','Original_Language','Poster_Url']

df.drop(cols, axis=1,inplace=True)
print(df.columns)
print(df.head())