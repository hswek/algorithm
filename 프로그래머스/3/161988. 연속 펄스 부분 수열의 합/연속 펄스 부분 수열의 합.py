def rec(left,right,arr):
    mid=(left+right)//2
    if left+1==right:
        return arr[left]
    result=9999999999999
    l=rec(left,mid,arr)
    r=rec(mid,right,arr)
    l_max=arr[mid-1]
    l_r=arr[mid-1]
    r_max=arr[mid]
    r_r=arr[mid]
    tmp=mid-2
    while tmp>=left:
        l_r+=arr[tmp]
        l_max=max(l_max,l_r)
        tmp-=1
    tmp=mid+1
    while tmp<right:
        r_r+=arr[tmp]
        r_max=max(r_max,r_r)
        tmp+=1
    return max([l_max+r_max,l,r])
def solution(seq):
    answer = 0
    arr1=[]
    for i in range(len(seq)):
        if i%2==0:
            arr1.append(seq[i])
        else:
            arr1.append(-seq[i])
    arr2=[]
    for i in range(len(seq)):
        if i%2==1:
            arr2.append(seq[i])
        else:
            arr2.append(-seq[i])
    answer=rec(0,len(seq),arr1)
    answer=max(answer,rec(0,len(seq),arr2))
    return answer