def solution(n):
    answer = 0
    start=0
    end=0
    s=0
    if n==1:
        return 1
    while True:
        if end>n:
            break
        if s<=n:
            if s==n:
                answer+=1
            end+=1
            s+=end
        else:
            while s>n and start<end:
                s-=start
                start+=1
                
    return answer