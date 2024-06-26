def solution(str1, str2):
    answer = 0
    arr1=[]

    for i in range(len(str1)-1):
        if str1[i].isalpha()==False or str1[i+1].isalpha()==False:
            continue
        arr1.append(str1[i:i+2].lower())
    d1={}
    for i in arr1:
        if i not in d1:
            d1[i]=1
        else:
            d1[i]+=1
    arr2=[]
    for i in range(len(str2)-1):
        if str2[i].isalpha()==False or str2[i+1].isalpha()==False:
            continue
        arr2.append(str2[i:i+2].lower())
    d2={}
    for i in arr2:
        if i not in d2:
            d2[i]=1
        else:
            d2[i]+=1
            
    just_arr1=list(set(arr1)-set(arr2))
    just_arr2=list(set(arr2)-set(arr1))
    arr1_arr2=list(set(arr1) & set(arr2))
    if len(arr1)==0 and len(arr2)==0:
        return 65536
    up=0
    low=0
    for i in arr1_arr2:
        up+=min(d1[i],d2[i])
    for i in arr1_arr2:
        low+=max(d1[i],d2[i])
    for i in just_arr1:
        low+=d1[i]
    for i in just_arr2:
        low+=d2[i]
    return int(up/low * 65536)
    
    
    
    return answer