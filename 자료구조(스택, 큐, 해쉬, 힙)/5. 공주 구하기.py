from collections import deque
n,k=map(int,input().split())
q=deque(i+1 for i in range(n))

while len(q)>1:
    for _ in range(k-1):
        q.append(q.popleft())
    q.popleft()
print(q[0])