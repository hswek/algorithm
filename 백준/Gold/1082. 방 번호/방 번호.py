import sys
from collections import deque
              
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
M=int(sys.stdin.readline().rstrip())
cache=[-1]*(M+1)
def recursive(m):
    if cache[m]!=-1:
        return cache[m]
    result=-1
    #print(m)
    result2=-1
    if m==M:
        a=1
    else:
        a=0
    for i in range(a,n):
        if m<arr[i]:
            continue
        #print(int(str(i) + str(recursive(m-arr[i]))))
        if result<int(str(i+1) + str(recursive(m-arr[i]))):
            result=int(str(i+1) + str(recursive(m-arr[i])))
            result2=str(i) + str(recursive(m-arr[i]))
    if result==-1:
        if m==M:
            return 0
        cache[m]=''
        return ''
    cache[m]=result2
    return result2
print(recursive(M))