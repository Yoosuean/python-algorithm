n=int(input())
arr=[[0]*(n+2) for _ in range(n+2)]

for i in range(1,n+1):
    tmp=map(int,input().split())
    arr[i][1:n+1]=tmp
cnt=0

# 배열탐색
for i in range(1,n+1):
    for j in range(1,n+1):
        target=arr[i][j]
        #상하좌우
        if arr[i-1][j]>=target or arr[i+1][j]>=target or arr[i][j-1]>=target or arr[i][j+1]>=target:
            continue
        else:
            cnt+=1
print(cnt)

 
'''
dx=[-1,0,1,0] #row
dy=[0,1,0,-1] #column
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.insert(0,[0]*n)
a.append([0]*n)
for x in a: 
    x.insert(0,0)
    x.append(0)
cnt=0

# 배열탐색
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): #상하좌우
            cnt+=1
print(cnt)
'''