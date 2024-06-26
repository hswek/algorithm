import math
def get_num(num):
    result=0
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            result+=2
    if math.sqrt(num) % 1==0:
        result-=1
    return result
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        tmp=get_num(i)
        #print(i,tmp)
        if tmp%2==0:
            answer+=i
        else:
            answer-=i
    return answer