def solution(num_list,limit):
    cnt=0
    max_val=0
    length=len(num_list)
    sort_list=sorted(num_list,reverse=True)
    while cnt<limit:
        for i in range(length):
            if sort_list[max_val]==num_list[length-i-1]:
                num_list[max_val],num_list[length-i-1]=sort_list[max_val],num_list[max_val]
                cnt+=1
                max_val+=1
                break
        if num_list==sort_list:
            break
    while cnt<limit:
        num_list[-1],num_list[-2]=num_list[-2],num_list[-1]
        cnt+=1
    return

t=int(input())

for i in range(t):
    num, limit=map(int,input().split())
    num_list=[j for j in map(int,str(num))]
    solution(num_list,limit)
    print(num_list)