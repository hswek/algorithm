import sys

arr=[[-1 for i in range(100)] for i in range(100)]
def comb(n,k):
    if n<0 or k<0:
        return 0
    if arr[n][k]!=-1:
        return arr[n][k]
    if n==k:
        return 1
    if k==1:
        return n
    arr[n][k]=comb(n-1,k)+comb(n-1,k-1)
    return arr[n][k]
n,k=map(int,input().split())
print(comb(n,k))