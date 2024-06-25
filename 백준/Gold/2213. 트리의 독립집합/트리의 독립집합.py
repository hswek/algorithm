import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n=int(sys.stdin.readline().rstrip())
node_value=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
d=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    d[a].append(b)
    d[b].append(a)
arr=[[] for i in range(n+1)]
q=deque()
q.append(1)
while(len(q)!=0):
    top=q.popleft()
    #print(top)
    for i in d[top]:
        if len(arr[i])==0:
            arr[top].append(i)
            q.append(i)
cache=[[-1]*2 for i in range(n+1)]

def make_adapter(root,color):
    if cache[root][color]!=-1:
        return cache[root][color]
    path=[root]
    result=0
    if color==1:
        tmp1=0
        for i in arr[root]:
            tmp1+=make_adapter(i,0)
        tmp1+=node_value[root]
        tmp2=0
        for i in arr[root]:
            tmp2+=make_adapter(i,1)

        result=max(tmp1,tmp2)
        
    if color==0:
        for i in arr[root]:
            result+=make_adapter(i,1)
    cache[root][color]=result
    
    return result
print_arr=[]        
        
a=make_adapter(1,1)
b=make_adapter(1,0)
if a>b:
    print(a)
else:
    print(b)
qq=deque()
qq.append(1)
#for i in cache:
    #print(i)
while len(qq)!=0:
    start=qq.popleft()
    if cache[start][0]<cache[start][1]:
        print_arr.append(start)
        for i in arr[start]:
            for j in arr[i]:
                qq.append(j)
    else :
        for i in arr[start]:
            qq.append(i)
print_arr.sort()
for i in print_arr:
    print(i,end=' ')