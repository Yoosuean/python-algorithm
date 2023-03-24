nums=list(range(21))

for _ in range(10):
    a,b=map(int,input().split())
    tmp=nums[a-1:b]
    tmp.reverse()
    nums[a-1:b]=tmp
for n in nums:
    print(n,end=" ")

'''
- reverse 함수 사용 X
nums=list(range(21))
for _ in range(10):
    a, b=map(int,input().split())
    for i in range((b-a+1//2)):
        nums[a+i], nums[b-i]=nums[b-i], nums[a+i]
nums.pop(0)
for n in nums:
    print(n,end=" ")
'''

'''
-입력예제
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20

-출력예제
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
'''