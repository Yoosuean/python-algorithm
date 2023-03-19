n=int(input())
nums=list(map(int,input().split()))
s=0
e=n-1
last=0
arr=[]
res=''

while s<=e:
    if nums[s]>last:
        arr.append((nums[s],'L'))
    if nums[e]>last:
        arr.append((nums[e],'R'))
    arr.sort()
    if len(arr)==0:
        break
    else:
        last=arr[0][0]
        res+=arr[0][1]
        if arr[0][1]=='L':
            s+=1
        else:
            e-=1
    arr.clear()
print(len(res))
print(res)

    