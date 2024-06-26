def solution(dartResult):
    answer = 0
    idx=0
    prev=0
    while idx<len(dartResult):
        first=int(dartResult[idx])
        if dartResult[idx+1]=='0':
            idx+=1
            first=10
        second=dartResult[idx+1]
        if second=='D':
            first=first*first
        elif second=='T':
            first=first*first*first
        if idx+2<len(dartResult) and not dartResult[idx+2].isdigit():
            if dartResult[idx+2]=='*':
                answer+=2*first
                answer+=prev
                prev=2*first
            elif dartResult[idx+2]=='#':
                answer-=first
                prev=-first
            idx+=3
        else:
            idx+=2
            answer+=first
            prev=first
        print(idx,answer)
    return answer