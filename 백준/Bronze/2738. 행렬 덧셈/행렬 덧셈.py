import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
arr1=[]
for i in range(n):
    arr1.append(list(map(int,sys.stdin.readline().rstrip().split())))
arr2=[]
for i in range(n):
    arr2.append(list(map(int,sys.stdin.readline().rstrip().split())))
for i in range(n):
    for j in range(m):
        print(arr1[i][j]+arr2[i][j],end=' ')
    print()