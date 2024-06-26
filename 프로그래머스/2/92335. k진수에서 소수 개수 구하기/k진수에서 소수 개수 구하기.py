import math
def is_prime(num):
    if num==1:
        return False
    if num==2:
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
def solution(n, k):
    answer = 0
    arr=[]
    while True:
        arr.append(n%k)
        n=n//k
        if n==0:
            break
    arr2=[]
    arr.reverse()
    now=0
    for i in arr:
        if i==0 :
            if now==0:
                continue
            arr2.append(now)
            now=0
            continue
        now*=10
        now+=i
    if now!=0:
        arr2.append(now)
    #print(arr2)
    for i in arr2:
        if is_prime(i)==True:
            #print('prime',i)
            answer+=1
            #print(answer)
        
    return answer