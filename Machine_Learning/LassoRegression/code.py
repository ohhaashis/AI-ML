from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error,r2_score
import pandas as pd
import numpy as np

insurance_data = pd.read_csv("LassoRegression/insurance.csv")

x = insurance_data.drop(columns=["charges"])
y = insurance_data["charges"]

x = pd.get_dummies(x,columns=["region"],drop_first=True)

x["sex"] = x["sex"].map({"female":1,"male":0})
x["smoker"] = x["smoker"].map({"yes":1,"no":0})

x["age_smoker"] = x['age']*x['smoker']
x["bmi_smoker"] = x['bmi']*x['smoker']

print(x.head())

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split (x,y,test_size=0.2,random_state=42)

lasso_model = Lasso(alpha=0.5)
lasso_model.fit(x_train,y_train)

y_pred = lasso_model.predict(x_test)

mse = mean_squared_error(y_test,y_pred)

# print(f"y-predicted : {y_pred}")
print(f"Mean squared error : {mse}")


#alpha = [i/10 for i in range(1,11)]
alpha = [0.001 , 0.1 , 1  ,2 , 5, 10 , 20 , 30 , 40 , 50 ,100]
mses = []

# for i in alpha:

#     lassoModel = Lasso(alpha=i)
#     lassoModel.fit(x_train,y_train)

#     y_Predicted = lassoModel.predict(x_test)

#     mSE_ = mean_squared_error(y_test,y_Predicted)

#     mses.append(mSE_)

#     print(f"MSE : {mSE_} for Alpha : {i}")

import seaborn as sns
import matplotlib.pyplot as plt

# sns.lineplot(x=alpha,y=mses,marker='o')
# plt.show()


from sklearn.linear_model import LassoCV

lasso_CVmodel = LassoCV(
    alphas = alpha ,
    cv = 5,
    max_iter = 1000,
    random_state = 42,
)

lasso_CVmodel.fit(x_train,y_train)

print(f"best alpha : {lasso_CVmodel.alpha_}")

y_Pred_CV = lasso_CVmodel.predict(x_test)
mse_cv = mean_squared_error(y_test,y_Pred_CV)

r2 = r2_score(y_test,y_Pred_CV)
print(f"r2 : {r2}")
print(f"Mean squared error of Lasso CV model : {mse_cv}")  