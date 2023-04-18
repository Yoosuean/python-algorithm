n,m=map(int,input().split())
rice=list(map(int,input().split()))

rice.sort()
s=0
e=rice[n-1]

while s<=e:
    mid=(s+e)//2
    sum=0
    for i in rice:
        if i>mid:
            sum+=i-mid
    if m>sum:
        e-=1
    else:
        res=mid
        s+=1
print(res)