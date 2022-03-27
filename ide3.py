import numpy as np
import pandas as pd
df=pd.read_csv('PlayTennis.csv')
print(df)
def find_entropy(df):
    #identify the target class name
    Class=df.keys()[-1]
    #identify the class values
    values=df[Class].unique() #yes or no
    entropy=0
    for value in values:
        prob=df[Class].value_counts()[value]/len(df[Class]) #|c|/|D|
        entropy+=prob*np.log2(prob)
    return entropy
def find_entropy_attribute(df,attribute):
    Class=df.keys()[-1]
    target_values=df[Class].unique() 
    #yes or no
    attribute_values=df[attribute].unique() 
    #all possible attribute values like sunny,rain,outcast
    avg_entropy=0
    for value in attribute_values: 
        #run with each possbile attribute values
        entropy=0
        for value1 in target_values: 
            #possible values
            num=len(df[attribute][df[attribute]==value][df[Class]==value1])
            den=len(df[attribute][df[attribute]==value])
            prob=num/den
            entropy+=-prob*np.log2(prob+0.000001) #to avoid zero error,add small value
        avg_entropy+=(den/len(df))*entropy
    return np.float(avg_entropy)
def find_most_promissing(df):
  IG=[]
  for key in df.keys()[:-1]:
      IG.append(find_entropy(df)-find_entropy_attribute(df,key))
      #print(IG)
  return df.keys()[:-1][np.argmax(IG)]
def get_subtable(df,attribute,value):
  return df[df[attribute]==value].reset_index(drop=True)
def buildtree(df,tree=None):
  tree=None
  node=find_most_promissing(df) #outlook is assigned to node
  #print(node)
  attvalue=np.unique(df[node])
  #print(attvalue)
  Class=df.keys()[-1] #identify the class column
  #print(Class)
  if tree is None: #if tree is None assign outlook as parent
      tree={}
      tree[node]={}
  #print(tree)
  for value in attvalue: #each possible value of attribute,create separate table
      subtable=get_subtable(df,node,value)
      Clvalue,counts=np.unique(subtable[Class],return_counts=True)
      if len(counts)==1: #if all lable are same stop the recursion
          tree[node][value]=Clvalue[0]
      else:
          tree[node][value]=buildtree(subtable) #build the subtree for the sub data set
  return tree
tree=buildtree(df)
df1=pd.read_csv('newdata.csv')
def predict(inst,tree):
  for node in tree.keys():
      value=inst[node]
      tree=tree[node][value]
      prediction=0
      if type(tree) is dict:
          prediction=predict(inst,tree)
      else:
          prediction=tree
  return prediction
Y_label=[]
for i in range(len(df1)):
  inst=df1.iloc[i,:]
  prediction=predict(inst,tree)
  Y_label.append(prediction)
print(Y_label)
