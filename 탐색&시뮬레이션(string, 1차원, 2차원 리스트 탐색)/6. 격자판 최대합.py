n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
res=[]

# 행과 열
for i in range(n):
    row_sum,column_sum=0,0
    for j in range(n):
        row_sum+=board[i][j]
        column_sum+=board[j][i]
    res.append(row_sum)
    res.append(column_sum)

# 대각선
sum1,sum2=0,0
for i in range(n):
    sum1+=board[i][i]
    sum2+=board[i][n-i-1]
res.append(max(sum1,sum2))

print(max(res))

'''
-입력예제
5
10 12 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 20 13 19

-출력예제
155
'''


'''
largest 변수를 선언하여 합을 구할 때 마다 최대값과 비교해주는 방법
largest=0
# 행과 열
for i in range(n):
    row_sum,column_sum=0,0
    for j in range(n):
        row_sum+=board[i][j]
        column_sum+=board[j][i]
    if row_sum>largest:
        largest=row_sum
    if column_sum>largest:
        lartgest=column_sum

# 대각선
sum1,sum2=0,0
for i in range(n):
    sum1+=board[i][i]
    sum2+=board[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    lartgest=sum2

print(largest)

'''