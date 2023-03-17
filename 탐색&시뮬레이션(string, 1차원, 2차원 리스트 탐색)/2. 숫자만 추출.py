s=input()
n=''
for x in s:
    if x.isdigit():
        n+=x
n=int(n)

cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1 
print(n,cnt,sep='\n')


'''
-입력예제
g0en2Ts8eSoft

-출력예제
28
6
'''
