import json

f = open('C:\KLA-Mock-Hackathon\Input data\level0.json')
 
data = json.load(f)

n=data["n_neighbourhoods"]

g=[]

g.append(data["restaurants"]["r0"]["neighbourhood_distance"])

for i in data["neighbourhoods"]:
    g.append(data["neighbourhoods"][i]["distances"])


def travellingsalesman(c):
    global cost
    global l
    adj_vertex = 99999
    min_val = 99999
    visited[c]=1
    l.append("n%d"%(c-1))
    for k in range(n):
        if (g[c][k] != 0) and (visited[k] == 0):
            if g[c][k] < min_val:
                min_val = g[c][k]
                adj_vertex = k
    if min_val != 99999:
        cost = cost + min_val
    if adj_vertex == 99999:
        adj_vertex = 0
        l.append("n%d"%(adj_vertex-1))
        cost = cost + g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)

cost = 0
l=[]
visited=[0]*(n+1)

travellingsalesman(0)

for i in range(len(l)):
    if l[i]=="n-1":
        l[i]="r0"
     

output={"v0":{"path":l}}

with open('output0.json', 'w') as f:
    json.dump(output, f)