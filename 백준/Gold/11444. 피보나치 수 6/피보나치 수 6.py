import sys
n=int(sys.stdin.readline().rstrip())
a=[[1,1],[1,0]]

def mul(a,b):
    n=2
    arr=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            s=0
            for z in range(n):
                s+=a[i][z]*b[z][j]%1000000007
            s=s%1000000007
            arr[i][j]=s
    return arr

def pow_2(arr,b):
    if b==1:
        return arr
    if b==2:
        return mul(arr,arr)
    tmp=pow_2(arr,b//2)
    if b%2==1:
        return mul(mul(tmp,tmp),arr)
    else:
        return mul(tmp,tmp)
arr2=pow_2(a,n)
print(arr2[0][1])
        