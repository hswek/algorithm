def solution(s):
    answer = ''
    d={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    idx=0
    while idx<len(s):
        if s[idx].isdigit():
            answer+=s[idx]
            idx+=1
        else:
            tmp=''
            while idx<len(s) and not s[idx].isdigit() and tmp not in d:
                tmp+=s[idx]
                idx+=1
            answer+=str(d[tmp])
    return int(answer)