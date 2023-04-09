N,M,K=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort(revers=True)

a=nums[0]
b=nums[1]
cnt=int(M/(K+1)*K)
cnt+=M%(K+1)

res=cnt*a
res+=(M-cnt)*b

print(res)
