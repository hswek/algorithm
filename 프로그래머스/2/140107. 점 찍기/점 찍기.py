import math
def solution(k, d):
    answer = 0
    for i in range(d+1):
        if i%k==0:
            #print(i,(d-i)//k+1)
            answer+= math.sqrt(d**2-i**2)//k+1
    return answer