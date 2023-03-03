def count_date(day):
    day=day.split(".")
    all_day=(int(day[0])*12*28)+(int(day[1])*28)+int(day[2])
    return all_day
 
def solution(today, terms, privacies):
    answer=[]
    terms_dict={}
    today=count_date(today)
    for i in terms:
        name,days=i.split()
        terms_dict[name]=int(days)*28

    for idx, privacy in enumerate(privacies):
        day, term=privacy.split(" ")
        day=count_date(day)
        day+=terms_dict[term]
        if today>=day:
            answer.append(idx + 1)
    return answer 