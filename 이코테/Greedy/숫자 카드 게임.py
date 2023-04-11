n,m=map(int,input().split())
res=[]

for _ in range(n):
    arr=list(map(int,input().split()))
    res.append(min(arr))
print(max(res))