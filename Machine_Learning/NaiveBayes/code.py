import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score, recall_score
from sklearn.naive_bayes import GaussianNB

heart_df = pd.read_csv("")
heart_df.head()

X = heart_df.drop('target',axis=1)
Y = heart_df['taregt']

x_train , x_test , y_train , y_test = train_test_split(
    X,Y , test_size=0.2 , random_state=42
)

### NAIVE BAYES 

gnb_model = GaussianNB()
gnb_model.fit(x_train,y_train)

y_pred = gnb_model.predict(x_test)

### EVALUATION

print(f"Recall score : {recall_score(y_test,y_pred)}")
print(f"Accuracy score : {accuracy_score(y_test,y_pred)}")
print(f"Precision score : {precision_score(y_test,y_pred)}") 