def solution(arr):
    #row, column 검사
    for i in range(9):
        tmp=[]
        arr_set=set(arr[i])
        if len(arr_set)!=9:
            return False
        for j in range(9):
            if arr[i][j] not in tmp:
                tmp.append(arr[i][j])
            else:
                return False

    # 3x3 검사
    r=0
    while r<=6:
        for i in range(3):
            tmp=[]
            for j in range(3):
                if arr[i+r][j+r] not in tmp:
                    tmp.append(arr[i+r][j+r])
                else:
                    return False
        r+=3
    return True

arr=[list(map(int,input().split())) for _ in range(9)]

if solution(arr):
    print("YES")
else:
    print("NO")