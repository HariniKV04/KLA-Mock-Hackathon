import json

f = open('C:\KLA-Mock-Hackathon\Input data\level1a.json')
 
data = json.load(f)

n=data["n_neighbourhoods"]
order=[]
capacity=data["vehicles"]["v0"]["capacity"]

g=[]


g.append(data["restaurants"][data["vehicles"]["v0"]["start_point"]]["neighbourhood_distance"])

for i in data["neighbourhoods"]:
    g.append(data["neighbourhoods"][i]["distances"])
    order.append(data["neighbourhoods"][i]['order_quantity'])

def travellingsalesman(c,cost,l):
    v=99999
    min=99999
    visited[c]=1
    l.append("n%d"%(c-1))
    for k in range(n):
        if (g[c][k] != 0) and (visited[k] == 0):
            if g[c][k] < min :
                min=g[c][k]
                v=k
    if min!=99999:
        cost+=min
    if v==99999:
        l.append("r0")
        cost+=g[c][0]
        return
    travellingsalesman(v,cost,l)


visited=[0]*(n+1)

cost=0
l=[]
travellingsalesman(0,cost,l)
    
l[0]="r0"
output={"v0":{"path":l}}

with open('output0.json', 'w') as f:
    json.dump(output, f)