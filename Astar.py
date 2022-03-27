graph={
    'A':[('B',2),('E',3)],'B':[('C',1),('G',9)],'C':None,'E':[('D',6)], 'D':[('G',1)] }
def find_neigh(node):
    if node in graph:
        return graph[node]
    else:
        return None

def H_val(node):
    H_dist={'A':11, 'B': 6, 'C':99, 'D': 1, 'E':7, 'G':0}
    return H_dist[node]

def aStar(I_node,D_node):
    OPEN=set(I_node)
    CLOSE=set()
    g={}
    p={}
    p[I_node]=I_node
    g[I_node]=0
    
    while len(OPEN)>0:
        n=None
        for v in OPEN:
            if n==None or g[v]+H_val(v)<g[n]+H_val(n):
                n=v
        if n==D_node or graph[n]==None:
            pass
        else:
            for(m,weight) in find_neigh(n):
                if m not in OPEN and m not in CLOSE:
                    OPEN.add(m)
                    p[m]=n
                    g[m]=weight+g[n]
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        p[m]=n
                    if m in CLOSE:
                        CLOSE.remove(m)
                        OPEN.add(m)
        if n==None:
            print("No path")
            return None
        if n==D_node:
            path=[]
                
            while p[n]!=n:
                path.append(n)
                n=p[n]
            path.append(I_node)
                
            path.reverse()
            print("Path: "+str(path))
            return path
        OPEN.remove(n)
        CLOSE.add(n)
            
    print('No path')
    return(None)

aStar('A','G')
