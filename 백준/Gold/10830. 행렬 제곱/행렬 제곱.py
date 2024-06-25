import sys
n,b=map(int,sys.stdin.readline().rstrip().split())
a=[]
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().rstrip().split())))

def mul(a,b):
    global n
    arr=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            s=0
            for z in range(n):
                s+=a[i][z]*b[z][j]%1000
            s=s%1000
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
arr2=pow_2(a,b)
for i in arr2:
    for j in i:
        print(j%1000,end=' ')
    print()
        