n=int(input())
nums=list(map(int,input().split()))
nums.sort()
t=1
for x in nums:
    if t<x:
        break
    t+=x
print(t)