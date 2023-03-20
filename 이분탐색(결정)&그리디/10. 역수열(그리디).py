n=int(input())
nums=list(map(int,input().split()))
res=[0]*n

for i in range(n):
    cnt=0
    tmp=nums[i]
    for j in range(n):
        if tmp==cnt and res[j]==0:
            res[j]=i+1
            break
        if res[j]==0:
            cnt+=1
        else:
            cnt+=0
for i in res:
    print(i, end=' ')

'''
-풀이
for i in range(n):
    for j in range(n):
        if nums[i]==0 and res[j]==0:
            res[j]=i+1
            break
        elif res[j]==0:
            res[i]-=1
for x in res:
    print(x, end=' ')
'''


'''
-입력예제
8
5 3 4 0 2 1 1 0

-출력예제
4 8 6 2 5 1 3 7
'''
