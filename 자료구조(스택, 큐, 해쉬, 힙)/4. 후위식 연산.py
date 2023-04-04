N=input()
stack=[]

for i in N:
    if i.isdecimal():
        stack.append(int(i))
    else:
        a=stack.pop()
        b=stack.pop()
        if i=='+':
            stack.append(b+a)
        elif i=='-':
            stack.append(b-a)
        elif i=='*':
            stack.append(b*a)
        else:
            stack.append(b/a)
print(stack[0])

