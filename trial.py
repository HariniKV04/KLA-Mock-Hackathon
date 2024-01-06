import json

f = open('C:\KLA-Mock-Hackathon\Input data\level0.json')
 
data = json.load(f)

n=data["n_neighbourhoods"]+len(data["restaurants"])
g=[]

g.append([0]+data["restaurants"][data["vehicles"]["v0"]["start_point"]]["neighbourhood_distance"])

for i in data["neighbourhoods"]:
    g.append([0]+data["neighbourhoods"][i]["distances"])
	
MAX = 999999

def TSP(mask, pos, graph, dp,n, visited):
	if mask == visited:
		return graph[pos][0]
	if dp[mask][pos] != -1:
		return dp[mask][pos]
	
	ans = MAX 
	for city in range(0, n):
		if ((mask & (1 << city)) == 0):
			new = graph[pos][city] + TSP(mask|(1<<city),city, graph, dp, n, visited)
			ans = min(ans, new)
	
	dp[mask][pos]=ans
	return dp[mask][pos]


visited = (1 << n) - 1
r,c=n*n,n
print(1<<n)
dp=[[-1 for j in range(c)]for i in range(r)]


print(TSP(1, 0,g, dp, n, visited))
