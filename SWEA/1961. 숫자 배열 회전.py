T=int(input())

for tc in range(T):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    arr_90=[[0]*N for _ in range(N)]
    arr_180=[[0]*N for _ in range(N)]
    arr_270=[[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            arr_90[i][j]=arr[N-1-j][i]
            arr_180[i][j]=arr[N-1-i][N-1-j]
            arr_270[i][j]=arr[j][N-1-i]
    print(f'#{tc+1}')
    for i in range(N):
        arr_90_str=list(map(str,arr_90[i]))
        arr_180_str=list(map(str,arr_180[i]))
        arr_270_str=list(map(str,arr_270[i]))
        print(''.join(arr_90_str),end=' ')
        print(''.join(arr_180_str),end=' ')
        print(''.join(arr_270_str))