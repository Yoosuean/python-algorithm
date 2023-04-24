n,m=map(int,input().split())
balls=list(map(int,input().split()))
cnt=0

for i in range(len(balls)):
    for j in range(i,len(balls)):
        if balls[i]!=balls[j]:
            cnt+=1
print(cnt)


'''
----- 교재답안
n,m=map(int,input().split())
data=list(map(int,input().split()))

array=[0]*11

for x in data:
    array[x]+=1
result=0
print(array)
for i in range(1,m+1):
    n-=array[i] 
    result+=array[i]*n
print(result)
'''