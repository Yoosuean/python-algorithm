n=list(input())
stack=[]
cnt=0

for i in range(len(n)):
    if n[i]=='(':
        stack.append(n[i])
    else:
        stack.pop()
        if n[i-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)
