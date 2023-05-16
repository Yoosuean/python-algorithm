#2019 KAKAO BLIND RECRUITMENT 실패율
def solution(N, stages):
    players=len(stages)
    dic_stage={}
    answer=[]
    for stage in stages:
        if stage in dic_stage:
            dic_stage[stage]+=1
        else:
            dic_stage[stage]=1
    for i in range(1,N+1):
        if i in dic_stage:
            failure_rate=dic_stage[i]/players
            players-=dic_stage[i]
        else:
            failure_rate=0
        answer.append((i,failure_rate))
    answer.sort(key=lambda x:(-x[1],x[0]))
    answer=[i[0] for i in answer]
    return answer