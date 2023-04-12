s=input()
N=8
column=ord(s[0])-97
row=int(s[1])-1
rule=[(-1,-2),(-2,-1),(1,2),(2,1),(-1,2),(1,-2),(2,-1),(-2,1)]
cnt=0

for r in rule:
    if column+r[0]>=0 and column+r[0]<N and row+r[1]>=0 and row+r[1]<N:
        cnt+=1
print(cnt)