n,m=map(int,input().split())
def a(arr,n,m):
    if m==0:
        for i in range(len(arr)):
            
            print(arr[i],end=' ')
        print()
        return
    for i in range(1,n+1):
        if i in arr:
            continue
        else:
            arr.append(i)
            a(arr,n,m-1)
            arr.pop()
    
arr=[]
a(arr,n,m)
