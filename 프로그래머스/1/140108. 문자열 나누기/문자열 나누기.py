def solution(s):
    answer = 0
    now=s[0]
    now_num=0
    else_num=0
    is_start=False
    for i in s:
        if is_start==True:
            is_start=False
            now=i
            
        if i==now:
            now_num+=1
        else:
            else_num+=1
        if now_num==else_num:
            answer+=1
            is_start=True
    if is_start==False:
        answer+=1
    
    return answer