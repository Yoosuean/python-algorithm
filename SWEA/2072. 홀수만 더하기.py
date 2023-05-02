t=int(input())

for i in range(t):
    sum=0
    nums=list(map(int,input().split()))
    for n in nums:
        if n%2!=0:
            sum+=n
    print('#{} {}'.format(i+1,sum))