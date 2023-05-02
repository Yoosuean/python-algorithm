t=int(input())

for _ in range(t):
    n=int(input())
    dic={}
    nums=map(int,input().split())

    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=0
    print('#{} {}'.format(n,max(dic,key=dic.get)))