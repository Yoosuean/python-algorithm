t=int(input())
for i in range(t):
    string=input()
    res=int(string==string[::-1])
    print(f'#{i+1} {res}')