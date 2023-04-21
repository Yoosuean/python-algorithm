s=list(map(int,input()))

for i in range(len(s)-1):
    a,b=s[i],s[i+1]
    if s[i]<=1:
        s[i+i]=a+b
    elif s[i+1]<=1:
        s[i+i]=a+b
    else:
        s[i+1]=a*b
print(s[-1])

'''
----- 교재답안
data=input()
result=int(data[0])

for i in range(1,len(data)):
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num
print(result)
'''