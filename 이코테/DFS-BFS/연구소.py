from collections import deque
import copy

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#바이러스 전파 경로
def bfs():
    queue=deque()
    tmp_graph=copy.deepcopy(graph)
    
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j]==2:
                queue.append((i,j))
    
    while queue:
        x, y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tmp_graph[nx][ny]==0:
                tmp_graph[nx][ny]=2
                queue.append((nx,ny))
    global res
    cnt=0

    #안전영역 최댓값
    for i in range(n):
        cnt+=tmp_graph[i].count(0)
    res=max(res,cnt)

# 빈공간 벽 설치
def makeWall(cnt):
    if cnt==3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]==1
                cnt+=1
                makeWall(cnt)
                graph[i][j]=0



n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
res=0
makeWall(0)
print(res)
