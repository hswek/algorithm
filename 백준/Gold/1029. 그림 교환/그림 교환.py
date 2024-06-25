import sys
from collections import deque
              
n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))
cache=[[[-1] * (10)for i in range(2**n+1) ] for i in range(n+1)]
#print(arr)
def recursive(pos,gone,prev_price):
    #print(pos,gone,prev)
    if cache[pos][gone][prev_price]!=-1:
        return cache[pos][gone][prev_price]
    result=0
    
    for i in range(n):
        #print(pos,i,prev)
        if gone & (1<<i) or arr[pos][i]<prev_price:
            continue
        result=max(result,recursive(i,gone + (1<<i),arr[pos][i])+1)
    cache[pos][gone][prev_price]=result
    return result
                                                                  
print(recursive(0,1,0)+1)