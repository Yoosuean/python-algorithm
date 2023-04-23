s=list(map(int,input()))
res=0

for x in range(1,len(s)):
    if s[x]!=s[x-1]:
        res+=1
if res==1:
    print(1)
elif res%2==0:
    print(res//2)
else:
    print(res//2+1)