for i in range(10):
    n=int(input())
    nums=list(map(int,input().split()))
    res=0
    for j in range(2,n-2):
        ch=[nums[j-2],nums[j-1],nums[j],nums[j+1],nums[j+2]]
        ch.sort(reverse=True)
        if nums[j]==ch[0]:
            res+=nums[j]-ch[1]
    print(f"#{i+1} {res}")          