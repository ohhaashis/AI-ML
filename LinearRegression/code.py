import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

insurance_data = pd.read_csv("LinearRegression/insurance.csv")

print(insurance_data.head(3))


## visualize 

# sns.scatterplot(data=insurance_data,x='bmi',y='charges',hue=insurance_data["smoker"])
# plt.show()

x = insurance_data.drop(columns=["charges","region"])
y = insurance_data["charges"]

print(x.head(3))
print(y.head(3))

x["sex"] = x["sex"].map({"female":1,"male":0})
x["smoker"] = x["smoker"].map({"yes":1,"no":0})


# Train test split

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# print(x_train.head())


# Train Model

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train,y_train)


## predict the values

y_pred = model.predict(x_test)
# print(y_pred)
# print(y_test)

## Evaluate

from sklearn.metrics import r2_score

r2  = r2_score(y_test,y_pred)
print("R^2 value :",r2)

#print(x_test.shape)

n = x_test.shape[0]
p = x_test.shape[1]

adjusted_R2 = 1 - ((1-r2**2)*(n-1)/(n-p-1))

print(f"Adjusted R**2 value : ",adjusted_R2)