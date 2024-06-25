import sys
string=sys.stdin.readline().rstrip()
arr=[[0]*27 for i in range(len(string))]
arr[0][ord(string[0])-ord('a')]+=1
for i in range(1,len(string)):
    for j in range(27):
        if j==ord(string[i])-ord('a'):
            arr[i][j]=arr[i-1][j]+1
        else:
            arr[i][j]=arr[i-1][j]
n=int(input())
for i in range(n):
    a,x,y=sys.stdin.readline().rstrip().split()
    x=int(x)
    y=int(y)
    if x==0:
        print(arr[y][ord(a)-ord('a')])
    else:
        print(arr[y][ord(a)-ord('a')]-arr[x-1][ord(a)-ord('a')])
