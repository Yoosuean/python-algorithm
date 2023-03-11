n=int(input())

for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))


    # if s==s[::-1]: # 문자열 reverse
    #     print("#%d YES" %(i+1))
    # else:
    #     print("#%d NO" %(i+1))
        

'''
-입력예제
5
level
moon
abcba
soon
gooG

-출력예제
#1 YES
#2 NO
#3 YES
#4 NO
#5 YES
'''

