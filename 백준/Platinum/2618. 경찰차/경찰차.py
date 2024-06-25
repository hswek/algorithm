import sys
from collections import deque
import heapq
#sys.setrecursionlimit(10**4)
n=int(sys.stdin.readline().rstrip())
e=int(sys.stdin.readline().rstrip())
arr=[[-1,-1]]
for i in range(e):
    i,j=map(int,sys.stdin.readline().rstrip().split())
    arr.append([i,j])

cache=[[-1]*(e+2) for i in range(e+2)]
print_arr=[[-1]*(e+2) for i in range(e+2)]
def recursive(a,b,pos):
    global e,print_arr,cache
    if cache[a][b]!=-1:
        return cache[a][b]
    if pos==e+1:
        return 0
    if a==0:
        car1=[1,1]
    else:
        car1=arr[a]
    if b==0:
        car2=[n,n]
    else:
        car2=arr[b]
    result=abs(arr[pos][0]-car1[0])+abs(arr[pos][1]-car1[1])+recursive(pos,b,pos+1)
    result2=abs(arr[pos][0]-car2[0])+abs(arr[pos][1]-car2[1])+recursive(a,pos,pos+1)
    cache[a][b]=min(result,result2)
    if result>=result2:
        print_arr[a][b]=2
    else:
        print_arr[a][b]=1
    return min(result,result2)
print(recursive(0,0,1))
start_a=0
start_b=0
while True:
    if start_a==e or start_b==e: 
        break
    if print_arr[start_a][start_b]==1:
        start_a=max(start_a,start_b)+1
        print(1)
    else:
        start_b=max(start_a,start_b)+1
        print(2)