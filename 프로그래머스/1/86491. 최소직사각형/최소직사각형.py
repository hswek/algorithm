def solution(sizes):
    answer = 0
    arr=[]
    for i in sizes:
        if i[1]>i[0]:
            arr.append([i[1],i[0]])
        else:
            arr.append([i[0],i[1]])
    max1=-1
    max2=-1
    for i in arr:
        if i[0]>max1:
            max1=i[0]
        if i[1]>max2:
            max2=i[1]
    answer=max1*max2
    
    return answer