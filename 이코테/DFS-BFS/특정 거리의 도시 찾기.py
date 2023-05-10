from collections import deque
import sys
input=sys.stdin.readline

def bfs(graph,start,distance):
    queue=deque([start])
    distance[start]=0
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if distance[i]==-1:
                distance[i]=distance[v]+1
                queue.append(i)

n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[-1]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

bfs(graph,x,distance)

ch=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        ch=True
if not ch:
    print(-1)

import heapq
import sys
input=sys.stdin.readline


'''
- 다익스트라
INF=int(1e9)
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

def dijkstra(s):
    q=[]
    heapq.heappush(q,(0,s))
    distance[s]=0
    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+1
            if cost<distance[i]:
                distance[i]=cost
                heapq.heappush(q,(cost,i))
dijkstra(x)

ch=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        ch=True
if not ch:
    print(-1)
'''