N = int(input())
d=(N//10)+1
res=0
for _ in range(d):
     res+=N%10
     N=N//10
print(res)