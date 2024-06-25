import sys
n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()
arr2=[0]*n
arr2[0]=arr[0]
for i in range(1,n):
    arr2[i]=arr2[i-1]+arr[i]
print(sum(arr2))