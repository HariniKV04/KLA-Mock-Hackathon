import json

f = open('C:\KLA-Mock-Hackathon\Input data\level1a.json')
 
data = json.load(f)
global n
n=data["n_neighbourhoods"]+1
global capacity
capacity=data["vehicles"]["v0"]["capacity"]


order=[]
g=[]

g.append([0]+data["restaurants"][data["vehicles"]["v0"]["start_point"]]["neighbourhood_distance"])

for i in data["neighbourhoods"]:
    g.append([0]+data["neighbourhoods"][i]["distances"])
    order.append(data["neighbourhoods"][i]["order_quantity"])

global paths
paths=[]
def travellingsalesman(c,cost,hold,l):
    v=99999
    min=99999
    visited[c]=1
    l.append("n%d"%(c-1))
    
    
    for k in range(1,n):
        if (g[c][k]!=0) and (visited[k]==0):
            if g[c][k]<min:  
                min=g[c][k]
                v=k
                    
    if v!=99999:
        hold+=order[v-1]
    if hold>capacity:
        print("Exceeding")
        l[0]="r0"
        l.append("r0")
        paths.append(l)
        l=[]
        cost=hold=0
        travellingsalesman(0,cost,hold,l)
        return 
    if sum(visited)==n:
        l[0]="r0"
        paths.append(l)
        print(paths)
    
    if min!=99999:
        cost+=min
    if v==99999:
        l.append("r0")
        cost+=g[c][0]
        return
    print("%d %d"%(v,hold))
    print(paths)
    
    travellingsalesman(v,cost,hold,l)
    
    

global visited
visited=[0]*(n+1)

cost=hold=0

l=[]
travellingsalesman(0,cost,hold,l)
    
output={"v0":{}}

for i in range(len(paths)):
    output["v0"]["path%d"%(i+1)]=paths[i]

with open('level1a_output.json','w') as f:
    json.dump(output, f)