def solution(babbling):
    answer = 0
    for s in babbling:
        idx=0
        now=-1
        while idx<len(s):
            if now!=1 and idx+3 <=len(s) and s[idx: idx+3] == 'aya':
                idx=idx+3
                now=1
                continue
            if now!= 2 and idx+2 <=len(s) and s[idx: idx+2] == 'ye':
                idx=idx+2
                now=2
                continue
            if now!= 3 and idx+3 <=len(s) and s[idx: idx+3] == 'woo':
                idx=idx+3
                now=3
                continue
            if now!= 4 and idx+2 <=len(s) and s[idx: idx+2] == 'ma':
                idx=idx+2
                now=4
                continue
            break
        if idx==len(s):
            print(s)
            answer+=1
            
        
    return answer