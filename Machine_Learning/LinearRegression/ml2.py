#  one hot encoding

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

insurance_data = pd.read_csv("LinearRegression/insurance.csv")

# print(insurance_data.head(3))


## visualize 

# sns.scatterplot(data=insurance_data,x='bmi',y='charges',hue=insurance_data["smoker"])
# plt.show()

x = insurance_data.drop(columns=["charges"])
y = insurance_data["charges"]

x = pd.get_dummies(x,columns=["region"],drop_first=True)

x["sex"] = x["sex"].map({"female":1,"male":0})
x["smoker"] = x["smoker"].map({"yes":1,"no":0})

x["age_smoker"] = x['age']*x['smoker']
x["bmi_smoker"] = x['bmi']*x['smoker']

print(x.head())


from sklearn.model_selection import train_test_split 

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
# print(y_pred)
# print(y_test)


from sklearn.metrics import r2_score

r2  = r2_score(y_test,y_pred)
print("R^2 value :",r2)

#print(x_test.shape)

n = x_test.shape[0]
p = x_test.shape[1]

adjusted_R2 = 1 - ((1-r2**2)*(n-1)/(n-p-1))

print(f"Adjusted R**2 value : ",adjusted_R2)

# underfit & overfit

# r2 training is low and testing is low - underfit
# r2 training is high and testing is low - overfit

y_train_pred = model.predict(x_train)
r2_train = r2_score(y_train,y_train_pred)
print(f"Training Data r2 : {r2_train}")
print(f"Test Data r2 : {r2}")