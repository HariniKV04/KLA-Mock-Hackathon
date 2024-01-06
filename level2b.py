import json

f = open('C:\KLA-Mock-Hackathon\Input data\level2b.json')
 
data = json.load(f)
global n
n=data["n_neighbourhoods"]+1
global capacity
capacity=[]

for i in data["vehicles"]:
    capacity.append(data["vehicles"][i]["capacity"])

o=[i for i in range(len(capacity))]

t=capacity[0]
for i in range(len(capacity)):
    for j in range(i+1,len(capacity)):
        if capacity[i]<capacity[j]:
            t=capacity[i]
            capacity[i]=capacity[j]
            capacity[j]=t

            t=o[i]
            o[i]=o[j]
            o[j]=t

order=[]
g=[]

g.append([0]+data["restaurants"][data["vehicles"]["v0"]["start_point"]]["neighbourhood_distance"])

for i in data["neighbourhoods"]:
    g.append([0]+data["neighbourhoods"][i]["distances"])
    order.append(data["neighbourhoods"][i]["order_quantity"])


cv=0



def travellingsalesman(c,cost,hold,l):
    global cv
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
    if hold>capacity[cv%len(capacity)]:
        l[0]="r0"
        l.append("r0")
        paths["v%d"%(o[cv%len(capacity)])]["path%d"%(len(paths["v%d"%(o[cv%len(capacity)])])+1)]=l

        cv+=1
        l=[]
        cost=hold=0
        travellingsalesman(0,cost,hold,l)
        return 
    if sum(visited)==n:
        l[0]="r0"
        paths["v%d"%(o[cv%len(capacity)])]["path%d"%(len(paths["v%d"%(o[cv%len(capacity)])])+1)]=l
    
    if min!=99999:
        cost+=min
    if v==99999:
        l.append("r0")
        cost+=g[c][0]
        return
    # print("%d %d"%(v,hold))
    # print(paths)
    
    travellingsalesman(v,cost,hold,l)
    
global paths
paths={}


global visited
visited=[0]*(n+1)

cost=hold=0

l=[]

for i in range(len(capacity)):
    paths["v%d"%i]=dict()

print(paths) 
travellingsalesman(0,cost,hold,l)
    
with open('level2b_output.json','w') as f:
    json.dump(paths, f)