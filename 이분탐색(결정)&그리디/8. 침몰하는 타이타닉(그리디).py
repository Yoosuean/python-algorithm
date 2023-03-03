from collections import deque
n,m=map(int,input().split())
w=list(map(int,input().split()))
w.sort()
w=deque(w)

cnt=0

while w:
    if len(w)==1:
       w.pop()
       cnt+=1
       break
    if w[0]+w[-1]<=m:
      w.popleft()
      w.pop()
      cnt+=1
    else:
       w.pop()
       cnt+=1
print(cnt)

'''
-입력예제
50 140
90 50 70 100 60

-출력예제
3
'''