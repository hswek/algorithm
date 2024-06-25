import sys

n,m=map(int,input().split())
arr=[]
arr2=[]
d={}
for i in range(n):
    s=sys.stdin.readline().rstrip()
    l=len(s)
    if l<m:
        continue
    if s not in d:
        d[s]=0
    else:
        d[s]+=1
arr3=d.items()
arr3=sorted(arr3,key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in range(len(arr3)):
    print(arr3[i][0])

    