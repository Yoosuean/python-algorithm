n=int(input())
nums=list(map(int,input().split()))
nums.sort()
cnt=0

while nums:
    for _ in range(nums[-1]):
        if nums:
            nums.pop()
        else:
            cnt-=1
    cnt+=1
print(cnt)

'''
----- 교재답안
n=int(input())
data=list(map(int,input().split()))
data.sort()
result=0
count=0

for i in data:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)
'''