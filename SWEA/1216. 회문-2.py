def solution(s):
    len = 1
    for i in range(100):  
        for j in range(len, 101):
            for k in range(101 - j):  
                word = s[i][k: k + j]
                if word == word[::-1]:
                    temp = len(word)
                    if len < temp:
                        len = temp
    return len


for _ in range(10):
    t = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    arr2 = list(map(list, zip(*arr)))
    col = solution(arr2)
    row = solution(arr)
    print('#{0} {1}'.format(t, max(row, col)))