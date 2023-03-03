L=int(input())
boxs=list(map(int,input().split()))
m=int(input())
boxs.sort()

for _ in range(m):
    boxs[0]+=1
    boxs[-1]-=1
    boxs.sort()

print(boxs[-1]-boxs[0])

'''
-입력예제
10
69 42 68 76 40 87 14 65 76 81
50

-출력예제
20
'''