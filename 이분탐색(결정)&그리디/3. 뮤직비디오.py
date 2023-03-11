def count(c):
    cnt=1
    sum=0
    for x in song:
        if sum+x>c:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt
    
n,m=map(int,input().split()) 
song=list(map(int,input().split()))

lt=1
rt=sum(song)
res=0

while lt<=rt:
    mid=(lt+rt)//2
    if count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)

'''
-입력예제
9 3
1 2 3 4 5 6 7 8 9

-출력예제
17
'''
