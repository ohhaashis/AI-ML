import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score

heart_df = pd.read_csv("")

heart_df.head()
heart_df.columns
heart_df.info()

heart_df['target'].nunique()

x = heart_df.drop("target")
y = heart_df['target']

# train test split 

x_train , x_test , y_train , y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

 
y_pred = model.predict(x_test)

print("accuracy :",accuracy_score(y_test,y_pred)*100)
print("Precission :",precision_score*100)

###################################################################################################################

# Scaling

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(x_train)
X_test = scaler.transform(x_test)

model.fit(X_train,y_train)
Y_pred = model.predict(X_test)

print("accuracy :",accuracy_score(y_test,Y_pred)*100)
print("Precission :",precision_score(y_test,Y_pred)*100)

######################################################################################################################

## Evaluation Metrics

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,precision_score,recall_score,f1_score

cm = confusion_matrix(y_test,y_pred)
print(cm)
print("Classification Report :",classification_report(y_test,y_pred))
print("Accuracy Score :",accuracy_score(y_test,y_pred))
print("Precision Score :",precision_score(y_test,y_pred))
print("Recall Score :",recall_score(y_test,y_pred))
print("F1 Score :",f1_score(y_test,y_pred))
