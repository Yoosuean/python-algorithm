# 기본 구현
n,m=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
for num in nums:
    if num==m:
        print(nums.index(num)+1)

# 이분탐색 
n,m=map(int,input().split())
nums=list(map(int,input().split()))
lt=0
rt=n-1

while lt<=rt:
    mid=(lt+rt)//2
    if nums[mid]==m:
        print(mid+1) # 몇번째라고 했으니 +1
        break
    elif nums[mid]>m:
        rt=mid-1
    else:
        lt=mid+1