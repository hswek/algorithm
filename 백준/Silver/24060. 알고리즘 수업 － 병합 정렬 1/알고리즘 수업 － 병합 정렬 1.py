import sys
haha=0
def merge_sort(arr,l,r):
    if l<r:
        m=(l+r)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)
def merge(arr,l,m,r):
    global haha,k
    if l==r:
        print('opps')
    tmp=[]
    i=l
    j=m+1
    tmp_num=0
    while(i<=m and j<=r):
        
        if arr[i]>=arr[j]:
            tmp.append(arr[j])
            tmp_num+=1
            j+=1
        else:
            tmp.append(arr[i])
            tmp_num+=1
            i+=1
    while(i<=m):
        tmp.append(arr[i])
        tmp_num+=1
        i+=1
    while(j<=r):
        tmp.append(arr[j])
        tmp_num+=1
        j+=1

    for ii in range(len(tmp)):
        arr[l+ii]=tmp[ii]
        haha+=1
        if haha==k:
            print(tmp[ii])
    
n,k =map(int,input().split())
arr=[]
arr=list(map(int,sys.stdin.readline().rstrip().split()))
merge_sort(arr,0,len(arr)-1)
if haha<k:
    print(-1)