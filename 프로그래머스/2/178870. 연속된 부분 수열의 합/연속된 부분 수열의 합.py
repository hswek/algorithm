def solution(sequence, k):
    answer = [-1,999999999999]
    s=0
    start=len(sequence)-1
    for i in range(len(sequence)-1,-1,-1):
        
        s+=sequence[i]
        #print(i,start,s)
        if s==k and start-i<=answer[1]-answer[0]:
            answer=[i,start]
        if s>k:
            while s>k:
                s-=sequence[start]
                start-=1
            if s==k and start-i<=answer[1]-answer[0]:
                answer=[i,start]
        
    return answer