# 그리디 : 정렬한 후 차례로 선택
 
n=int(input())
times=[]
for _ in range(n):
    s,e=map(int,input().split())
    times.append((s,e))
    
times.sort(key=lambda x : (x[1],x[0])) # 끝나는 시간을 기준으로
et=0
cnt=0

for s,e in times:
    if s>=et:
        et=e
        cnt+=1
print(cnt)


