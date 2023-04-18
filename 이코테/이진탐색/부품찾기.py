def solution(s,e,target):
    while s<=e:
        mid=(s+e)//2
        if target==nums[mid]:
            print('yes',end=' ')
            return
        elif target>nums[mid]:
            s=mid+1
        else:
            e=mid-1
    print('no',end=' ')
    return

n=int(input())
nums=list(map(int,input().split()))
m=int(input())
targets=list(map(int,input().split()))
nums.sort()

for target in targets:
    s=0
    e=n-1
    solution(s,e,target)

'''
----- 계수정렬
n=int(input())
arr=[0]*1000001
for i in input().split():
    arr[int(i)]=1

m=int(input())
t=list(map(int,input().split()))

for i in t:
    if arr[i]==1:
        print("yes",end=' ')
    else:
        print("no",end=' ')

        

----- 집합
n=int(input())
arr=set(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))

for i in t:
    if i in arr:
        print("yes",end=' ')
    else:
        print("no",end=' ')
'''