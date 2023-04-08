a=input()
b=input()
s=dict()

for x in a:
    if x in s.keys():
        s[x]+=1
    else:
        s[x]=1

for x in b:
    if x in s.keys():
        s[x]-=1
    else:
        s[x]=1

for val in s.values():
    if val!=0:
        print("NO")
        break
else:
    print("YES")