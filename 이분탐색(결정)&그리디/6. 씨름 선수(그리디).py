
N=int(input())
users=[]
for _ in range(N):
    h,w=map(int,input().split())
    users.append((h,w))
users.sort(reverse=True)
largest=0
cnt=0
for h,w in users:
    if w>largest:
        largest=w
        cnt+=1
print(cnt)