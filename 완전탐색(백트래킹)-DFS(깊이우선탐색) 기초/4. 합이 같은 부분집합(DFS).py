import sys
def DFS(L,a_sum):
    if a_sum>total//2: # total을 넘기면 더이상 계산하지 않아도 됨.
        return
    if L==n:
        if a_sum==(total-a_sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1,a_sum+a[L])
        DFS(L+1,a_sum)

n=int(input()) # 6
a=list(map(int,input().split())) # 1 3 5 6 7 10
total=sum(a)
DFS(0,0) 
print("NO")

