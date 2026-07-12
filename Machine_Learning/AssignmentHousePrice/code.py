import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error


dataH = pd.read_csv("AssignmentHousePrice/HousePricePrediction.csv")

#dataH.fillna(0,inplace=True)

# Subclass_mode = dataH['MSZoning'].mode()[0]
# dataH['MSZoning'] = dataH['MSZoning'].fillna(Subclass_mode)

# LotConfig_mode = dataH['LotConfig'].mode()[0]
# dataH['LotConfig'] = dataH['LotConfig'].fillna(LotConfig_mode)

# BldgType_mode = dataH['BldgType'].mode()[0]
# dataH['BldgType'] = dataH['BldgType'].fillna(BldgType_mode)

# Exterior1st_mode = dataH['Exterior1st'].mode()[0]
# dataH['Exterior1st'] = dataH['Exterior1st'].fillna(Exterior1st_mode)

# dataH['MSSubClass'] = dataH['MSSubClass'].fillna(dataH['MSSubClass'].median())
# dataH['LotArea'] = dataH['LotArea'].fillna(dataH['LotArea'].median())
# dataH['OverallCond'] = dataH['OverallCond'].fillna(dataH['OverallCond'].median())
# dataH['YearBuilt'] = dataH['YearBuilt'].fillna(dataH['YearBuilt'].median())
# dataH['YearRemodAdd'] = dataH['YearRemodAdd'].fillna(dataH['YearRemodAdd'].median())
# dataH['BsmtFinSF2'] = dataH['BsmtFinSF2'].fillna(dataH['BsmtFinSF2'].median())
# dataH['TotalBsmtSF'] = dataH['TotalBsmtSF'].fillna(dataH['TotalBsmtSF'].median())

dataH.drop(['Id'],axis=1,inplace=True)

dataH['SalePrice'] = dataH['SalePrice'].fillna(dataH['SalePrice'].median())
dataH = dataH.dropna()

cols = ['MSZoning','LotConfig','BldgType','Exterior1st']
dataH = pd.get_dummies(dataH,columns=cols,drop_first=True)


print(dataH.head(3))

# sns.scatterplot(data = dataH , x = 'LotArea' , y = 'SalePrice')
# plt.show()

x = dataH.drop(["SalePrice"],axis=1)
y = dataH["SalePrice"]

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=0)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

r2 = r2_score(y_test,y_pred)
print(f"R**2 value is : {r2}")


n = x_test.shape[0]
p = x_test.shape[1]
adjusted_r2 =   1 - ((1-r2**2)*(n-1)/(n-p-1))

print(f"Adjusted R**2 value is : {adjusted_r2}")

print(f"Mean Absolute error : {mean_absolute_error(y_test,y_pred)}")
print(f"Mean Absolute error : {np.sqrt(mean_squared_error(y_test,y_pred))}")
print(f"Mean Absolute error : {mean_absolute_percentage_error(y_test,y_pred)}")

