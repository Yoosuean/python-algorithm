t=int(input())
for i in range(t):
    c=input()
    cnt=0
    bit='0'
    for x in c:
        if x!=bit:
            cnt+=1
        bit=x
    print(f'#{i+1} {cnt}')