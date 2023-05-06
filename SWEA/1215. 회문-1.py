for k in range(10):
    n=int(input())
    board=[list(str(input())) for _ in range(8)]
    board2=list(zip(*board))
    res=0

    for i in range(8):
        for j in range(8-n+1):
            if board[i][j:j+n]==board[i][j:j+n][::-1]:
                res+=1
            if board2[i][j:j+n]==board2[i][j:j+n][::-1]:
                res+=1
    print(f'#{k+1} {res}')            
