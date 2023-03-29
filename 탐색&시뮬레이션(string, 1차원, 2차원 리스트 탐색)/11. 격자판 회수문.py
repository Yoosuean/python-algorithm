arr=[input().split() for _ in range(7)]
cnt=0

# 가로탐색
for i in range(7):
    for j in range(3):
        if arr[i][j]==arr[i][j+4] and arr[i][j+1]==arr[i][j+3]:
            cnt+=1

# 세로탐색
for i in range(7):
    for j in range(3):
        if arr[j][i]==arr[j+4][i] and arr[j+1][i]==arr[j+3][i]:
            cnt+=1
print(cnt)


'''
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        # 가로탐색
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        # 세로탐색
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)
'''