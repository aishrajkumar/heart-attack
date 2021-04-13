# -*- coding: utf-8 -*-

# -- Sheet --

# Dataset from https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


df = pd.read_csv('./heart.csv')
df['age']=df['age'].div(10)
df['trtbps']=df['trtbps'].div(100)
df['chol']=df['chol'].div(100)
df['thalachh']=df['thalachh'].div(100)
df.head()

# Age : Age of the patient
# 
# Sex : Sex of the patient
# 
# exang: exercise induced angina (1 = yes; 0 = no)
# 
# ca: number of major vessels (0-3)
# 
# cp : Chest Pain type chest pain type
# 
# Value 1: typical angina Value 2: atypical angina Value 3: non-anginal pain Value 4: asymptomatic trtbps : resting blood pressure (in mm Hg)
# 
# chol : cholestoral in mg/dl fetched via BMI sensor
# 
# fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
# 
# rest_ecg : resting electrocardiographic results
# 
# Value 0: normal Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria thalach : maximum heart rate achieved
# 
# target : 0= less chance of heart attack 1= more chance of heart attack


# 





plt.figure(figsize = (12,12))
df.boxplot()

df["trtbps"].hist()
df["chol"].hist()

plt.figure(figsize = (12,12))
sns.heatmap(df.corr(),annot=True)

# 




# 70% Training 
# 
# 15% Testing 
# 
# 15% Validation


from sklearn.model_selection import train_test_split
import numpy as np

X = df.drop("output", axis=1).to_numpy()
y = df["output"].to_numpy()

# Splitting the dataset to our desired proportions
X_train, X_test_val, y_train, y_test_val = train_test_split(X, y,train_size=0.70, test_size=0.3, random_state=0)

X_valid, X_test, y_valid, y_test = train_test_split(X_test_val, y_test_val,train_size=0.50, test_size=0.5, random_state=0)

# Logistic Regression
from sklearn.linear_model import LogisticRegression

#(Possible solution) For better accuracy: attempt to scale. 
#clf= classifier
LR = LogisticRegression(solver='lbfgs', max_iter=1000)
clf= LR.fit(X_train, y_train)
clf.predict(X[:2,:])
clf.score(X_train, y_train)
#LR = LogisticRegression(random_state=0).fit(X_train, y_train)

# Random Forest Regressor
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=400, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# 



#Random Forest Classifier 
#https://stackabuse.com/random-forest-algorithm-with-python-and-scikit-learn/
from sklearn.ensemble import RandomForestClassifier

regressor = RandomForestClassifier(n_estimators=400, random_state=5)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

#Neural Net Multi-layer Perceptron (MLP)
#https://scikit-learn.org/stable/modules/neural_networks_supervised.html

from sklearn.neural_network import MLPClassifier
clf_mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, 
                        hidden_layer_sizes=(5,2), random_state=1)

clf_mlp.fit(X_train, y_train)
clf_mlp.predict(X[:2,:])
clf_mlp.score(X_train, y_train)

#SVM 
from sklearn import svm

#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
print(accuracy_score(y_test, y_pred))


#Minimize bottom-left (false-positives)


from sklearn.metrics import plot_confusion_matrix
plt.figure(figsize = (12,12))
plot_confusion_matrix(clf_mlp, X_test, y_test)  
plt.show()

#Next Steps
# - Multicoliearity
# - Outliers (Min false-positives)  -> Adjust class weights or hyperparameter tuning
# - Comfortable w/ ~89-92 accuracy
# - Understand models (i.e., neural net, forest, etc...): More ensemble methods
# - Work on scaling 

