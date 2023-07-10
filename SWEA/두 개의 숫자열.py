T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    a_list=list(map(int,input().split()))
    b_list=list(map(int,input().split()))
    max=0
    if N>M:
        N,M=M,N
        a_list,b_list=b_list,a_list
    
    for j in range(M-N+1):
        tmp=0
        for k in range(N):
            tmp+=a_list[k]*b_list[k+1]
        
        if tmp>max:
            max=tmp
    print("#{} {}".format(i+1,max))