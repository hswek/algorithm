def solution(n, m, section):
    answer = 0 
    now=section[0]-1
    for i in section:
        #print(now,i)
        if now<i:
            
            now=i+m-1
            answer+=1
        
    return answer