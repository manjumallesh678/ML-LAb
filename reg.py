import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('10-dataset.csv')
data.head()

colA=np.array(data.total_bill)
print(colA)

colB=np.array(data.tip)
print(colB)

mcolA=np.mat(colA)
mcolB=np.mat(colB)
np.shape(mcolA)
m=np.shape(mcolB)[1]
one=np.ones((1,m),dtype=int)
X=np.hstack((one.T,mcolA.T))

def kernal(point,xmat,k):
    m,n=np.shape(xmat)
    weights=np.mat(np.eye((m)))
    for j in range(m):
        diff = point-X[j]
        weights[j,j]=np.exp(diff*diff.T/(-2.0*k**2))
    return weights

def localWeight(point,xmat,ymat,k):
    wt=kernal(point,xmat,k)
    W=(X.T*(wt*X)).I*(X.T*wt*ymat.T)
    return W

def localWeightRegression(xmat,ymat,k):
    m,n=np.shape(xmat)
    ypred=np.zeros(m)
    for i in range(m):
        ypred[i]=xmat[i]*localWeight(xmat[i],xmat,ymat,k)
    return ypred

ypred = localWeightRegression(X, mcolB , 0.5)

xsort=X.copy()
xsort.sort(axis=0)
plt.scatter(colA,colB,color='blue')
plt.plot(xsort[:,1],ypred[X[:,1].argsort(0)],color='yellow',linewidth=5)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
