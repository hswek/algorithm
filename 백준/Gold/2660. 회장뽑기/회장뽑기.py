import sys
from collections import deque
sys.setrecursionlimit(10000)
n=int(sys.stdin.readline().rstrip())
arr=[[99999999999999]*(n) for i in range(n)]
while True:
    i,j=map(int,sys.stdin.readline().rstrip().split())
    if i==-1 and j==-1:
        break
    i-=1
    j-=1
    arr[i][j]=1
    arr[j][i]=1
for i in range(n):
    arr[i][i]=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])
ans=[99999999999999]*(n)
for i in range(n):
    ans[i]=max(arr[i])
min_ans=min(ans)
result=0
for i in range(n):
    if min_ans==ans[i]:
        result+=1
print(min_ans,result)
for i in range(n):
    if min_ans==ans[i]:
        print(i+1,end=' ')