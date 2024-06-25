import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
result=0
for i in range(n-1,-1,-1):
    while k>=arr[i]:
        k-=arr[i]
        result+=1
    if k==0:
        break
print(result)
               