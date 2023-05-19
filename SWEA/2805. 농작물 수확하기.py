
def solution(n,nums):
    global res
    if n==1:
        res=nums[0][0]
        return
    tmp=n//2
    res+=sum(nums[tmp])
    for i in range(tmp):
        res+=sum(nums[i][tmp-i:n-tmp+i])
        res+=sum(nums[n-1-i][tmp-i:n-tmp+i])
    return

t=int(input())
for i in range(t):
    n=int(input())
    nums=[]
    res=0
    for _ in range(n):
        nums.append(list(map(int,str(input()))))
    solution(n,nums)
    print(f'#{i+1} {res}')
