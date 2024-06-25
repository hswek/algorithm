import sys
sys.setrecursionlimit(10**5)
n,m,start=map(int,sys.stdin.readline().rstrip().split())
arr=[[] for i in range(n+1)]
for i in range(m):
    i,j=map(int,sys.stdin.readline().rstrip().split())
    arr[i].append(j)
    arr[j].append(i)
for i in range(1,n+1):
    arr[i].sort(reverse=True)
visit=[0]*(n+1)
num=1
def dfs(start):
    global num
    visit[start]=num
    num+=1
    for i in arr[start]:
        if visit[i]!=0:
            continue
        else:
            dfs(i)
dfs(start)
for i in range(1,n+1):
    print(visit[i])