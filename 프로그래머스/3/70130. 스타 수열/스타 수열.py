def is_star(arr):
    tmp=[]
    if len(arr)%2!=0:
        return False
    for i in range(len(arr)//2):
        if arr[2*i]==arr[2*i+1]:

            return False
        tmp.append({arr[2*i],arr[2*i+1]})
    s=tmp[0]
    for t in tmp:
        s=s&t
    if len(s)==0:
        return False
    return True

        
def solution(arr):
    answer = 0
    d={}
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    l=list(d.items())
    l.sort(key=lambda x:-x[1])
    dd={}
    for i in range(min(5,len(l))):
        start=l[i][0]
        tmp=0
        idx=0
        if i in dd:
            continue
        dd[i]=True
        while idx<len(arr)-1:
            if (arr[idx]==start or arr[idx+1]==start) and arr[idx]!=arr[idx+1]:
                idx+=2
                tmp+=1
            else:
                idx+=1
        answer=max(answer,tmp*2)
    return answer