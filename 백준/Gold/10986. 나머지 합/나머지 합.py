import sys
n,k=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr2=[0]*(n)
arr2[0]=arr[0]%k
d={}
d[arr2[0]]=1
for i in range(1,n):
    arr2[i]=(arr2[i-1]+arr[i])%k
    
    if arr2[i] in d:
        d[arr2[i]]+=1
    else:
        d[arr2[i]]=1
result=0
#print(arr2)
#print(d)
for i in range(n):
    if arr2[i]==0:
        result+=1
for i in d.values():
    #print(i)
    if i<=1:
        continue
    result+=(i)*(i-1)//2
print(result)