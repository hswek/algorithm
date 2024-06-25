#x,y,z=map(int,input().split())
n=int(input())
arr=[0]*5001
arr[1]=-1
arr[2]=-1
arr[3]=1
arr[4]=-1
arr[5]=1

for i in range(6,5001):
    a=arr[i-3]
    b=arr[i-5]
    if a==-1 and b==-1:
        arr[i]=-1
    elif a==-1:
        arr[i]=b+1
    elif b==-1:
        arr[i]=a+1
    elif a>b:
        arr[i]=b+1
    else:
        arr[i]=a+1
    
print(arr[n])
