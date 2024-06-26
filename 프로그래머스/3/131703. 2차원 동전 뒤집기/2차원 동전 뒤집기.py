def bit_count(num):
    result=0
    while num!=0:
        if num%2==1:
            result+=1
        num=num>>1
    return result
import copy
def is_same(a,b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]!=b[i][j]:
                return False
    return True
def flip(start,end,r):
    n=len(start)
    for i in range(n):
        if (r & (1<<i)):
            for j in range(len(start[0])):
                if start[i][j]==1:
                    start[i][j]=0
                else:
                    start[i][j]=1
    result=0
    for i in range(len(start[0])):
        if [r[i] for r in start]==[r[i] for r in end]:
            continue
        elif [1-r[i] for r in start]==[r[i] for r in end]:
            result+=1
        else:
            return -1
    return result
    if is_same(start,end):
        return True
    return False
def solution(beginning, target):
    answer = 100000000
    n=len(beginning)
    for i in range(2**n):
        tmp=flip(copy.deepcopy(beginning),target,i)
        if tmp!=-1:
            answer=min(answer,bit_count(i)+tmp)
    if answer==100000000:
        return -1
    return answer