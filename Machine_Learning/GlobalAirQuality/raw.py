import numpy as np
import pandas as pd

df = pd.read_csv("GlobalAirQuality/raw_data.csv")

#print(df.isnull())
#print(df.isna())

#print(df.isna().sum())
#print(df.isnull().sum())

#print(df.dropna()) # row drop
#print(df.dropna(axis =1 )) # column drop

# age_mean = df["age"].mean()
# p = df["age"].fillna(age_mean)
# print(p)

########################

# isnull()/isna()
#  isnull().sum()
# dropna()

# fillna(value)
# ffill()
#  bfill()


##########################

# duplicated
# drop_duplicates()

