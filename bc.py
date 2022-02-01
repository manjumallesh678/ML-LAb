import pandas as pd

df=pd.read_csv('PlayTennis9.csv')
print(df)
print(len(df))

targetAttribute=df.keys()[-1]
df[targetAttribute]

possibleTargetValues=df[targetAttribute].unique()
print(possibleTargetValues)

PriProb={}
for eachPossibleValues in possibleTargetValues:
    PriProb[eachPossibleValues]=df[targetAttribute][df[targetAttribute]==eachPossibleValues].count()/len(df)
print(PriProb)

finalProb={}
for eachAttribute in df.keys()[:-1]:  #outlook,temp,humid,wind
    finalProb[eachAttribute]={}
    for eachPossibleValues in df[eachAttribute]:  #sunny...
        finalProb[eachAttribute][eachPossibleValues]={}
        for eachPossibleTargetValues in possibleTargetValues:  #no,yes
            finalProb[eachAttribute][eachPossibleValues][eachPossibleTargetValues]=df[eachAttribute][df[eachAttribute]==eachPossibleValues][df[targetAttribute]==eachPossibleTargetValues].count()/df[targetAttribute][df[targetAttribute]==eachPossibleTargetValues].count()

testdata=pd.read_csv('PlayTennis9 - Copy.csv')
print(testdata)

probyesno={}
for eachPossibleTargetValues in possibleTargetValues:  #yes and no
    prob=1
    probyesno[eachPossibleTargetValues]={}
    for eachTestAttribute in testdata.keys():  #Outlook,temp,humid,wind
        prob=prob*finalProb[eachTestAttribute][testdata.iloc[0][eachTestAttribute]][eachPossibleTargetValues]
    prob=prob*PriProb[eachPossibleTargetValues]
    probyesno[eachPossibleTargetValues]=prob

probyesno
             


            

