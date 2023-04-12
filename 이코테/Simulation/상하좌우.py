n=int(input())
arr=[list(i for i in range(n)) for j in range(n)]
d=input().split()
column=0
row=0
target=arr[row][column]

for i in d:
    if i=='L':
        if column>0:
            column-=1
    elif i=='R':
        if column<n-1:
            column+=1
    elif i=='U':
        if row>0:
            row-=1
    else:
        if row<n-1:
            row+=1
    target=arr[row][column]
print(row+1,column+1,sep=' ')

'''
- 교재 답안
n=int(input())
x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny

print(x,y)
'''