for _ in range(10):
    n=int(input())
    nums=[list(map(int,input().split())) for i in range(100)]
    res=0
    tmp1=0
    tmp2=0
    sum_nums=[]
    for i in range(100):
        #가로
        sum_nums.append(sum(nums[i]))
        #대각선
        tmp1+=nums[i][i]
        tmp2+=nums[i][99-i]    
    sum_nums.append(tmp1)
    sum_nums.append(tmp2)

    #세로
    for i in range(100):
        tmp=0
        for j in range(100):
            tmp+=nums[j][i]
        sum_nums.append(tmp)
    print(f'#{n} {max(sum_nums)}')

