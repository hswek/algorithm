from itertools import permutations
import math
def is_prime(num):
    if num==0:
        return False
    if num==1:
        return False
    if num==2:
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
def solution(numbers):
    answer = 0
    arr=list(numbers)
    parr=[]
    for i in range(1,len(numbers)+1):
        parr+=list(permutations(arr,i))
    #print(parr)
    d={}
    for num in parr:
        tmp=int(''.join(num))
        if tmp not in d and is_prime(tmp):
            #print(tmp)
            d[tmp]=True
            answer+=1
            
    
    return answer