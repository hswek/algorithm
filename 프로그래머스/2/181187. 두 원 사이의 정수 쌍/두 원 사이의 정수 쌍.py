import math
def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        if r1>i:
            
            start= math.ceil(math.sqrt(r1**2 -i**2))
        else:
            start=0
        end= math.floor(math.sqrt(r2**2 -i**2))
        answer=answer+end-start+1
    answer*=4
        
    return answer