import sys
n=int(input())
arr=[-1]*1001
arr[0]=0
arr[1]=1
arr[2]=2
def a(n):
    if n==2:
        return 2
    if n==1:
        return 1
    if arr[n]!=-1:
        return arr[n]
    arr[n]=a(n-1)+a(n-2)
    return arr[n]
a(100)
a(300)
a(500)
a(800)
a(n)
print(arr[n]%10007)