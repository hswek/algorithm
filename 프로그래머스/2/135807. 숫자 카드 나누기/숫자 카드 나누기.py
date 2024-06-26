import math
def all_devided(arr,i):
    for num in arr:
        if num%i!=0:
            return False
    return True
def all_not_devided(arr,i):
    for num in arr:
        if num%i==0:
            return False
    return True
def solution(arrayA, arrayB):
    answer = 0
    mina=min(arrayA)
    minb=min(arrayB)
    tmp=[]
    for i in list(range(2,int(math.sqrt(mina))+1))+[mina]:  
        if mina%i==0:
            tmp.append(mina//i)
            if all_devided(arrayA,i) and all_not_devided(arrayB,i):
                answer=max(answer,i)
    for i in tmp:
        if all_devided(arrayA,i) and all_not_devided(arrayB,i):
            answer=max(answer,i)
            
    tmp=[]
    for i in list(range(2,int(math.sqrt(minb))+1))+[minb]:  
        if minb%i==0:
            tmp.append(minb//i)
            if all_devided(arrayB,i) and all_not_devided(arrayA,i):
                answer=max(answer,i)
    for i in tmp:
        if all_devided(arrayB,i) and all_not_devided(arrayA,i):
            answer=max(answer,i)
    
    return answer