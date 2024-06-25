import sys
def merge_sort(arr,l,r):
    if l<r:
        m=(l+r)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)
def merge(arr,l,m,r):
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

    
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
merge_sort(arr,0,len(arr)-1)
for i in range(n):
    print(arr[i])