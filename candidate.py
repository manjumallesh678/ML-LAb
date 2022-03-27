import csv
data = []
with open('data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)
print(data)
row = len(data)
col = len(data[0]) - 1

sh = ['0']*col
gh = ['?']*col

for feature in range(0,col):
    sh[feature]=data[0][feature]
temp = []
for sample in range(0,row):
    cr = data[sample]
    
    if cr[-1] == 'yes':
        for feature in range(0,col):
            if sh[feature] != data[sample][feature]:
                sh[feature] = '?'
        for feature in range(0,col):
            for k in range(0,len(temp)):
                if sh[feature] != temp[k][feature] and temp[k][feature] != '?':
                    del temp[k]
    elif cr[-1] == 'no':
        for feature in range(0,col):
            if sh[feature] != data[sample][feature]:
                gh[feature] = sh[feature]
                temp.append(gh)
                gh = ['?']*col
    print("----------------------------------------------------------------")
    print('Row=',sample)
    print('Specific hypothesis:',sh)
    if len(temp)==0:
        print('General hypothesis:',gh)
    else:
        print('General hypothesis:',temp)
    print("----------------------------------------------------------------")
