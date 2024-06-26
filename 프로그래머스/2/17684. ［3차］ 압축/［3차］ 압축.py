def solution(msg):
    answer = []
    d={}
    for i in range(ord('Z')-ord('A')+1):
        d[chr(ord('A')+i)]=i+1
    now=27
    idx=0

    while idx<len(msg):
        s=msg[idx]
        idx+=1
        if idx==len(msg):
            answer.append(d[s])
    
        while idx<len(msg):
            if s+msg[idx] not in d:
                answer.append(d[s])
                d[s+msg[idx]]=now
                now+=1
                break
            else:
                s+=msg[idx]
                idx+=1
                if idx==len(msg):
                    answer.append(d[s])
                
                
    return answer