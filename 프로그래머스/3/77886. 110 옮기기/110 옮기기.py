def solution(s):
    answer = []
    for string in s:
        now=''
        idx=0
        c=0
        while idx<len(string):
            if now[-2:]=='11' and string[idx]=='0': 
                c+=1
                now=now[:-2]
            else:
                now+=string[idx]
            idx+=1
        idx=now.find('111')
        if idx!=-1:
            answer.append(now[:idx]+'110'*c + now[idx:])
        else:
            idx=now.rfind('0')
            answer.append(now[:idx+1]+'110'*c + now[idx+1:])
    return answer