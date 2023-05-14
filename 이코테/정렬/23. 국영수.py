#BOJ 18310 국영수
import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    name,a,b,c=input().split()
    arr.append((name,int(a),int(b),int(c)))
arr.sort(key=lambda x : (-x[1],x[2],-x[3],x[0]))
for i in arr:
    print(i[0])