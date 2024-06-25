result=0
n=int(input())
arr=[0]*n
def is_set_queen(arr,i,x):

    arr[x]=i
    for i in range(x):
        if arr[i]==arr[x]:
            return False
        elif (x-i)==abs(arr[i]-arr[x]):
            return False
    return True
    
def queen(arr,line,n):
    global result
    if line==n-1:
        for i in range(n):
            if visit[i]==0 and is_set_queen(arr,i,line):
                result+=1
        return
    for i in range(n):
        if visit[i]==0 and is_set_queen(arr,i,line):
            visit[i]=1
            queen(arr,line+1,n)
            visit[i]=0
visit=[0]*n
queen(arr,0,n)
print(result)