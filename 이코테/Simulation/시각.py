# 경우의 수가 100,000도 되지 않으므로 완전탐색
# 탐색 데이터가 100만개 이하일 때 완전탐색 적절

n=int(input())
cnt=0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if i%10==3 or j%10==3 or k%10==3:
                cnt+=1
            elif j//10==3 or k//10==3:
                cnt+=1
print(cnt)
            

'''
- 교재 답안
h=int(input())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)
'''