import math
def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        num=0
        for j in range(1,int(math.sqrt(i))+1):
            if i%j==0:
                num+=1
                if j==i//j:
                    num-=0.5
        num=num*2
        if num>limit:
            num=power
        #print(i,num)
        answer+=num
    return answer