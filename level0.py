import json

f = open('C:\KLA-Mock-Hackathon\Input data\level0.json')
 
data = json.load(f)

n=data["n_neighbourhoods"]+len(data["restaurants"])
g=[]

g.append([0]+data["restaurants"][data["vehicles"]["v0"]["start_point"]]["neighbourhood_distance"])

for i in data["neighbourhoods"]:
    g.append([0]+data["neighbourhoods"][i]["distances"])

def travellingsalesman(c,cost,l):
    v=99999
    min=99999
    visited[c]=1
    l.append("n%d"%(c-1))
    for k in range(n):
        if (g[c][k] != 0) and (visited[k] == 0):
            if g[c][k] < min:
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

with open('level0_output.json', 'w') as f:
    json.dump(output, f)