n,m=map(int,input().split())
nums=list(map(int,input().split()))
cnt=0
test=0

for i in range(n):
    for j in range(n):
        tmp=sum(nums[i:j+1])
        if tmp==m:
            cnt+=1
            break
        if tmp>m:
            break
print(cnt)


'''
- 루프 도는 횟수 최소
n,m=map(int,input().split())
a=list(map(int,input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
test=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)
'''