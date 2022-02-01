Graph_d={
    'A':[('B','C'),'D'],
    'B':[('G','H')],
    'C':None,
    'D':[('E','F')],
    'I':None,
    'G':None,
    'H':None,
    'E':['I'],
    'F':None
}   

def H_val(node):
    if node in H_dist:
        return H_dist[node]
    
H_dist={
    'A':5,'B':3,'C':4,'D':5,'G':5,'H':7,'E':4,'F':4,'G':5,'I':0
}
NH={}
NH=H_dist
Visited=[]
label={}
parent={}
label={'A':'NS','B':'NS','C':'NS','D':'NS','E':'NS','F':'NS','G':'NS','H':'NS','I':'NS'}
H_dist1={
    'A':5,'B':3,'C':4,'D':5,'G':5,'H':7,'E':4,'F':4,'G':5,'I':0
}
l='NS'
def AO_star(node):
    
    global F
    global l
    val=0
    print('************************')
    print('Expanding',node)
    Visited.append(node)
   
    #if the node is a terminal node
    if Graph_d[node]==None:
        F=H_val(node)
        NH[node]=H_val(node)+1
        print(node,'return',H_val(node)+1)
        #if the node h value is 0 mark it as soloved 
        if H_dist1[node]==0:
            l='S'
        return [H_val(node)+1,l]
        
    
    #if the node is having child nodes
    else:
        for SUCC in Graph_d[node]:
            print('SUCC',SUCC)
            if len(SUCC) ==1:
                v,l=AO_star(SUCC)
                val=val+v
                label[SUCC]=l
                print('H:',H_dist[SUCC])
                NH[node]=val
                print(node,'returns',val)
                parent[SUCC]=node
            else:
                i=0
                for n in SUCC:
                    v,l=AO_star(n)
                    val=val+v
                    parent[n]=node
                    label[n]=l
                    print(SUCC,':',i)
                NH[node]=val
                print(node,'returns',val)
        NH[node]=val
        return val,l
NH['A'],label['A']=AO_star('A')
path=[]
for k,v in label.items():
    if v == 'S':
        path.append(k)
        
if label['A']=='NS':
    print('We cannot solve the graph')
else:
    print(path)
