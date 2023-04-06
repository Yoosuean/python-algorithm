from collections import deque
t=input()
n=int(input())

for i in range(n):
    x=input()
    dq=deque(t)
    for j in x:
        if j in dq:
            if j!=dq.popleft():
                print(f"#{i+1} NO")
                break
    else:
        if len(dq)==0:
            print(f"#{i+1} YES")
        else:
            print(f"#{i+1} NO")