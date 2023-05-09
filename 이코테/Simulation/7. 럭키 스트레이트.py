N=int(input())
nums=list(int(i) for i in str(N))
d=len(nums)//2
if sum(nums[0:d])==sum(nums[d:d*2]):
    print("LUCKY")
else:
    print("READY") 