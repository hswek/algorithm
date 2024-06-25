import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
cache=[[-1]*100001 for i in range(101)]
def knap_sack(k,v):
    if cache[v][k]!=-1:
        return cache[v][k]
    result=0
    for i in range(v,len(arr)):
        if arr[i][0]<=k:
            result=max(result,arr[i][1]+knap_sack(k-arr[i][0],i+1))
    cache[v][k]=result
    return result
print(knap_sack(m,0))