# 이분검색은 결정 알고리즘이라는 방법론에서 사용.
# 결정 알고리즘의 특징? 우리가 찾고자 하는 답이 특정 범위 안에 있음을 알 수 있음.
# Ex. a~b사이 내에 답이 있다. 

def count(len):
    cnt=0
    for x in lines:
        cnt+=(x//len)
    return cnt

k,n=map(int,input().split())
lines=[int(input()) for _ in range(k)]

lt=1
rt=max(lines)

while lt<=rt:
    mid=(lt+rt)//2
    if count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)