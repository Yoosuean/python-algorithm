# 부분집합 구해서 최대값 확인, 전위순회
import sys
input=sys.stdin.readline

def DFS(l,arr_sum,tsum):
    global res
    if res<arr_sum+(total-tsum): # 시간복잡도를 줄이기 위해서 추가
        return                   # 적용된 바둑이 부분집합의 합 - 적용할 바둑이 부분집합의 합
    if arr_sum>c:
        return
    if l==n:
        if res<arr_sum:
            res=arr_sum
        return
    else:
        DFS(l+1,arr_sum+arr[l],tsum+arr[l])
        DFS(l+1,arr_sum,tsum+arr[l])


c,n=map(int,input().split())
arr=[0]*n
for i in range(n):
    arr[i]=int(input())
res=0
total=sum(arr)
DFS(0,0,0)
print(res)