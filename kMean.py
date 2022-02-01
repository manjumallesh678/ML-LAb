import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
import pandas as pd
import numpy as np

iris = datasets.load_iris()

print("\n Iris data:", iris.data)
print("\n Iris features:\n",iris.feature_names)
print("\n Iris target:\n",iris.target)
print("\n Iris names:\n",iris.target_names)
X=pd.DataFrame(iris.data)
X.columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
Y=pd.DataFrame(iris.target)
Y.columns=['Target']

plt.figure(figsize=(14,7))
colormap = np.array(['red','lime','black'])

plt.subplot(1,2,1) #1 row,2 columns and do operations on 1st position
plt.scatter(X.sepal_length,X.sepal_width,c=colormap[Y.Target])
plt.title('Sepal')
plt.subplot(1,2,2) #1 row,2 columns and do operations on 2nd position
plt.scatter(X.petal_length,X.petal_width,c=colormap[Y.Target])
plt.title('Petal')
plt.show() #to print sepal and petal together

model=KMeans(n_clusters=3)
model.fit(X)
model.labels_

l1=[0,1,2]
def rename(s):
    l2=[]
    for i in s:
        if i not in l2:
            l2.append(i)
    for i in range(len(s)):
        pos=l2.index(s[i])
        s[i]=l1[pos]
    return s

km=rename(model.labels_)
print("\n What kMeans thought:\n",km)
print("Accuracy of KMeans is",sm.accuracy_score(Y,km))
print("Confusion matrix for KMeans is \n",sm.confusion_matrix(Y,km))

from sklearn import preprocessing

scaler=preprocessing.StandardScaler()
scaler.fit(X)
xsa=scaler.transform(X)
xs=pd.DataFrame(xsa,columns=X.columns)
print("\n",xs.sample(5))

from sklearn.mixture import GaussianMixture
gmm=GaussianMixture(n_components=3)
gmm.fit(xs)

Y_cluster_gmm=gmm.predict(xs)

plt.subplot(1,2,1)
plt.scatter(X.petal_length,X.petal_width,c=colormap[Y_cluster_gmm])
plt.title('GMM Classification')
plt.show()

em=rename(Y_cluster_gmm)
print("\n What EM thought:\n",em)
print("Accuracy of EM is ",sm.accuracy_score(Y,em))
print("Confusion matrix for EM is \n",sm.confusion_matrix(Y,em))
