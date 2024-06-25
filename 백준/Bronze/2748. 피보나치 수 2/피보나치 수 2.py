n=int(input())
arr=[-1]*(n+1)
def fibo(n):
    if n==1:
        return 1
    if n==0:
        return 0
    if arr[n]!=-1:
        return arr[n]
    else:
        arr[n]=fibo(n-1)+fibo(n-2)
        return arr[n]
print(fibo(n))