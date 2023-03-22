n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))
res=sorted(n_list+m_list)
for i in res:
    print(i,end=" ")

'''
p1=p2=0
c=[]
while p1<n and p2<m:
    if n_list[p1]<=m_list[p2]:
        c.append(n_list[p1])
        p1+=1
    else:
        c.append(m_list[p2])
        p2+=1
if p1<n:
    c=c+n_list[p1:]
if p2<m:
    c=c+m_list[p2:]
for x in c:
    print(x,end=" ")
'''

'''
-입력예제
3
1 3 5
5
2 3 6 7 9

-출력예제
1 2 3 3 5 6 7 9
'''