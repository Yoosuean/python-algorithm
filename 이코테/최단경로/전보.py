import heapq

INF=int(1e9)
n,m,s=map(int,input().split())

graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(s):
    q=[]
    heapq.heappush(q,(0,s))
    distance[s]=0
    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(s)

cnt=0
max_val=0
for d in distance:
    if d!=INF:
        cnt+=1
        max_val=max(d,max_val)
print(cnt-1,max_val)