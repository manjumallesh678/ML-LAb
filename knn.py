import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

names=['sepal-length','sepal-width','petal-length','petal-width','Class']
dataset=pd.read_csv('iris.data',names=names)
print(dataset)

X=dataset.iloc[:,:-1]
Y=dataset.iloc[:,-1]
print(X.head())
Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.10)

classifier=KNeighborsClassifier(n_neighbors=5).fit(Xtrain,Ytrain)
Ypred=classifier.predict(Xtest)

i=0
print("\n----------------------------------------")
print('%-25s %-25s %-25s' %('Original Label','Predicted Label','Correct/Wrong'))
print("------------------------------------------")

for label in Ytest:
    print('%-25s %-25s' %(label,Ypred[i]),end="")
    if (label==Ypred[i]):
        print('%-25s' %('Correct'))
    else:
        print('%-25s' %('Wrong'))
    i=i+1
print("-----------------------------------------")
print("\n Confusion matrix:\n",metrics.confusion_matrix(Ytest,Ypred))
print("------------------------------------------")
print("\n Classification report:\n", metrics.classification_report(Ytest,Ypred))
print("-------------------------------------------")
print('Accuracy of the classifier is %0.2f' %metrics.accuracy_score(Ytest,Ypred))
print("-----------------------------")
