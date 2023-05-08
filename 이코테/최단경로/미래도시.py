INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

x,k=map(int,input().split())

for i in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])

res=graph[0][k-1]+graph[k-1][x-1]
if res==INF:
    print(-1)
else:
    print(res)
        