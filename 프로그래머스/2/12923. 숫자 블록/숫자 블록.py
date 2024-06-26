import math
def max_num(i):
    if i==1:
        return 0
    tmp=1
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            tmp=max(j,tmp)
            if i//j<=10000000:
                tmp=max(tmp,i//j)
                #break
    return tmp
def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        answer.append(max_num(i))
    return answer