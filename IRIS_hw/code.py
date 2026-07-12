import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

flower_df = pd.read_csv('IRIS_hw/Iris.csv')

print(flower_df.head())

# print(flower_df.info())
# print(flower_df.isnull())

X = flower_df.drop("Species",axis=1)
Y = flower_df['Species']

# Train Test Split

from sklearn.model_selection import train_test_split

X_train , X_test , Y_train , Y_test = train_test_split(
    X,Y,test_size=0.5, random_state=42
)


######################################################################### Logistic Regression 

from sklearn.linear_model import LogisticRegression

# model = LogisticRegression(max_iter=1000)
# model.fit(X_train,Y_train)

# Y_pred = model.predict(X_test)

# ## Evaluating

from sklearn.metrics import accuracy_score,precision_score,recall_score,classification_report
from sklearn.metrics import classification_report,confusion_matrix

# print(f"LOGISTIC REG ")
# print(f" Recall Score : {recall_score(Y_test,Y_pred,average='macro')}")
# print(f"Accuracy : {accuracy_score(Y_test,Y_pred)}")
# print(f"Precision Score : {precision_score(Y_test,Y_pred,average='macro')}")
# print(f"cm : {confusion_matrix(Y_test,Y_pred)}")
# print(f"Classification report : {classification_report(Y_test,Y_pred)}")

# ### checking if model is not cheating

from sklearn.model_selection import cross_val_score

# scores = cross_val_score(model,X,Y,cv=5)

# print(f"All cross-validation scores : {scores}")
# print(f"True avg accuracy : {scores.mean()*100}") 

###################################################################################### =>  KNN 

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

scalar = StandardScaler()

x_train_scaled = scalar.fit_transform(X_train)
x_test_scaled = scalar.transform(X_test)

knn_classifier = KNeighborsClassifier(n_neighbors=5)

knn_classifier.fit(x_train_scaled,Y_train)

y_pred = knn_classifier.predict(x_test_scaled)

print(f"KNN")
print(f" Recall Score : {recall_score(Y_test,y_pred,average='macro')}")
print(f"Accuracy : {accuracy_score(Y_test,y_pred)}")
print(f"Precision Score : {precision_score(Y_test,y_pred,average='macro')}")
print(f"Precision Score : {precision_score(Y_test,y_pred,average='macro')}")
print(f"cm : {confusion_matrix(Y_test,y_pred)}")
print(f"Classification report : {classification_report(Y_test,y_pred)}")

# ## cross check

from sklearn.model_selection import cross_val_score

# scores = cross_val_score(knn_classifier,x_scaled,Y,cv=5)
# print(f"All cross validation scores : {scores}")
# print(f"True Avg Accuracy : {scores.mean()*100}")


###################################################################################### NAIVE BAYES

from sklearn.naive_bayes import GaussianNB

# gnb_model = GaussianNB()

# gnb_model.fit(X_train,Y_train)

# y_pred = gnb_model.predict(X_test)

# print(f" Recall Score : {recall_score(Y_test,y_pred,average='macro')}")
# print(f"Accuracy : {accuracy_score(Y_test,y_pred)}")
# print(f"Precision Score : {precision_score(Y_test,y_pred,average='macro')}")


# scores = cross_val_score(gnb_model,X,Y,cv=5)
# print(f"All cross validation scores : {scores}")
# print(f"True Avg Accuracy : {scores.mean()*100}")