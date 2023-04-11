res=[]

def solution(n):
    tmp=n%2
    n=n//2
    res.append(tmp)
    if n<=1:
        res.append(n)
        return
    solution(n)

n=int(input())
solution(n)
for i in reversed(res):
    print(i,end="")

'''
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2,end='')
n=int(input())
DFS(n)
'''