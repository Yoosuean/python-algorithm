n,m=map(int,input().split())
a,b,d=map(int,input().split())
ch=[[0]*m for _ in range(n)]
ch[a][b]=1
res=0

# 맵 정보
m=[]
for _ in range(n):
    m.append(list(map(int,input().split())))

# 북서남동
dx=[-1,0,1,0]
dy=[0,-1,0,1]

# 1.왼쪽으로 돌기 북서남동 0321 
# 2.바다인지, 방문했는지 확인
# 3.방문했거나 바다면 1으로 돌아감
# 4.방문하지 않았으면 전진
# 5. 1로 돌아감
# 6. 네 방향이 모두 바다인경우, 모두 방문한경우 바라보는 방항을 유지한 채로 한칸 뒤로간 후 1단계
# 7. 뒤쪽 방향이 바다거나 갈 수 없는 경우 움직임 멈춤

# 왼쪽으로 회전
def turn_left():
    global d
    d-=1
    if d==-1:
        d==3

# 방문확인
def check_visited():
    global a,b,res
    if ch[a+dx[d]][b+dy[d]]==0 and m[a+dx[d]][b+dy[d]]==0:
        a+=dx[d]
        b+=dy[d]
        ch[a][b]=1
        res+=1
        return True
    return False 

# 뒤로 갈 수 있는지 확인
def back():
    global a,b,d
    d-=2
    if d<0:
        d+=4
    if m[a+dx[d]][b+dy[d]]==0:
        a+=dx[d]
        b+=dx[d]
        return False
    return True
    
while True:
    # 현재 바라보는 방향 제외하고 체크
    for i in range(3):
        turn_left()
        isVisited=check_visited()
        # 전진할 수 있는 네방향을 모두 방문했거나 바다인 경우 멈춤
        if i==2 and not isVisited:
            isStop=back()
    if isStop:
        break
print(res+1)