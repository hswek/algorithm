def get_result(users,emoticons,discount):
    plus=0
    expense=0
    for limit,num in users:
        pay=0
        for d in range(l):
            if discount[d]>=limit:
                pay+=emoticons[d]*(100-discount[d])/100
        if pay>=num:
            plus+=1
        else:
            expense+=pay
    global answer_plus,answer_expense
    if answer_plus<plus:
        answer_plus=plus
        answer_expense=expense
    elif answer_plus==plus and answer_expense<expense:
        answer_expense=expense
def dfs(users,emoticons,discount):
    if len(discount)==l:
        get_result(users,emoticons,discount)
        return
    for i in [10,20,30,40]:
        discount.append(i)
        dfs(users,emoticons,discount)
        discount.pop()
    return 
def solution(users, emoticons):
    global l,answer_plus,answer_expense
    l=len(emoticons)
    answer_plus=0
    answer_expense=0
    dfs(users,emoticons,[])
    return [answer_plus,answer_expense]