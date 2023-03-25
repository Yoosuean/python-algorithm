import copy
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
res=copy.deepcopy(arr)
m=int(input())

# 회전
for _ in range(m):
    row,p,r=map(int,input().split())
    row-=1
    if p==0:
        for i in range(n):
            tmp=i+(r%n)
            if tmp>=n:
                res[row][i]=arr[row][tmp-n]  
            else:
                res[row][i]=arr[row][tmp]  
    else:
        for i in range(n):
            tmp=i-(r%n)
            if tmp>=0:
                res[row][i]=arr[row][tmp]  
            else:
                res[row][i]=arr[row][n-abs(tmp)] 

# 모래시계 더하기
total=0
for i in range(n//2):
    total+=sum(res[i][i:n-i])+sum(res[n-1-i][i:n-i])
total+=res[n//2][n//2]

print(total)


'''
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())

# 회전
for i in range(m):
    h,t,k=map(int,input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop())

# 모래시계 더하기
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(res)
'''