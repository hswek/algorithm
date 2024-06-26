import math
def solution(brown, yellow):
    answer = []
    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow%i==0:
            #print(i,(i+1) , (1+(yellow//i)))
            if (i+2) * (2+(yellow//i))==(brown+yellow):
                return [2+(yellow//i),i+2]
    return answer