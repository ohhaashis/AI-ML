import pandas as pd
from sklearn.metrics import precision_score,recall_score,accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

heart_df = pd.read_csv('')

heart_df.head()

x = heart_df.drop('target',axis=1)
y = heart_df['taarget']

x_train , x_test , y_train , y_test = train_test_split(
    x,y,test_size=0.2 , random_state=42
)

scalar = StandardScaler()

x_train_scaled = scalar.fit_transform(x_train)
x_test_scaled = scalar.fit_transform(x_test)

knn_classifier  = KNeighborsClassifier(n_neighbors=3)

knn_classifier.fit(x_train,y_train)

y_pred = knn_classifier.predict(x_test_scaled)



#### cross validation for hyperparameter tuning using grid search

from sklearn.model_selection import GridSearchCV

classifier = KNeighborsClassifier()
param_grid = {'n_neighbours':[3,5,7,9]}

ClassifierCV = GridSearchCV(
    classifier,
    param_grid,
    cv=5,
    # if scoring -> parameter
    scoring='recall'
)

ClassifierCV.fit(x_train_scaled,y_train)

Y_Pred = ClassifierCV.predict(x_test_scaled)


print(f"Recall score : {recall_score(y_test,y_pred)}")
print(f"Accuracy score : {accuracy_score(y_test,y_pred)}")
print(f"Precision score : {precision_score(y_test,y_pred)}") 

## results

res = pd.DataFrame(ClassifierCV.cv_results_)

print(f"Results : {res[['param_n_neighbours','mean_test_score']]}")

print(f"Best parameter : {ClassifierCV.best_params_}")


#### PIPELINE

from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

X_train , X_test , Y_train , Y_test = train_test_split(
    x,y ,test_size=0.2 , random_state=42
)


pipeline = Pipeline([
    ('scalar',StandardScaler(),
     ('knn',KNeighborsClassifier()))
])

param_grid = {'knn__n_neighbours':[3,5,7,9]}

ClassifierCV = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    # if scoring -> parameter
    scoring='recall'
)

ClassifierCV.fit(X_train,Y_train)

Y_Pred = ClassifierCV.predict(X_test)


print(f"Recall score : {recall_score(Y_test,Y_Pred)}")
print(f"Accuracy score : {accuracy_score(Y_test,Y_Pred)}")
print(f"Precision score : {precision_score(Y_test,Y_Pred)}") 