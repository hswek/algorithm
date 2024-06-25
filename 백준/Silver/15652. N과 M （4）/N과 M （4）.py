n,m=map(int,input().split())
def a(arr,n,m,idx):
    if m==0:
        for i in range(len(arr)):
            
            print(arr[i],end=' ')
        print()
        return
    for i in range(idx,n+1):
        arr.append(i)
        a(arr,n,m-1,i)
        arr.pop()
    
arr=[]
a(arr,n,m,1)
