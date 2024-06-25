import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n=int(sys.stdin.readline().rstrip())

d=[[] for i in range(n+1)]
node_value=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))

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

cache=[[-1]*(3) for i in range(n+1)]
def make_adapter(root,what):
    #print(root,what)
    if cache[root][what]!=-1:
        return cache[root][what]
    great=2
    cool=1
    not_cool=0
    result=0
    if what==great:
        for i in arr[root]:
            result+=make_adapter(i,cool)
        result+=node_value[root]
        #return result
    elif what==cool:
        
        for i in arr[root]:
            result+=make_adapter(i,not_cool)
        
    elif what==not_cool:
        #자신이 우수마을이 아님,이웃중에 하나가 우수임
        max_num=0
        for i in arr[root]:
            tmp=0
            tmp+=make_adapter(i,great)

            for j in arr[root]:
                if i==j:
                    continue
                tmp+=make_adapter(j,not_cool)
            max_num=max(max_num,tmp)
        #자신이 우수마을임
        for i in arr[root]:
            result+=make_adapter(i,cool)
        result+=node_value[root]
        result=max(result,max_num)
    #print(root,what,result)
    cache[root][what]=result
    return result
#print(arr)
print(max(make_adapter(1,2),make_adapter(1,0)))
    
    

