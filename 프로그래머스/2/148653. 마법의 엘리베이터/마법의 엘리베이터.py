def solution(storey):
    answer = 0
    s=storey
    while True:
        if s==0:
            break
        a=s%10
        if a>=6:
            answer+=(10-s%10)
            s=s//10
            s+=1

        elif a==5 and s//10%10>=5:
            answer+=(10-s%10)
            s=s//10
            s+=1
        else:
            
            answer+=s%10
            s=s//10
        
            
    answer+=s
    return answer