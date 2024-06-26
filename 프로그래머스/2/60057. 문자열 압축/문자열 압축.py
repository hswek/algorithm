def get_length(l,s):
    tmp=''
    idx=0
    now=s[idx:idx+l]
    repeat=1
    idx+=l
    while idx<len(s):
        if now==s[idx:idx+l]:
            idx+=l
            repeat+=1
        else:
            if repeat!=1:
                tmp+= str(repeat)+now
            else:
                tmp+=now
            now=s[idx:idx+l]
            idx+=l
            repeat=1
    if repeat!=1:
        tmp+= str(repeat)+now
    else:
        tmp+=now
    #print(tmp)
    return len(tmp)
    
def solution(s):
    answer = 999999999999999999999
    for l in range(1,len(s)+1):
        #print(l,get_length(l,s))
        answer=min(answer,get_length(l,s))
        
    return answer