s=list(input())

num=0
for i in range(len(s)):
    if s[i].isdigit():
        num+=int(s[i])
        s[i]=''
s.sort()
print(''.join(s),num,sep='')
