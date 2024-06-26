def solution(N, stages):
    answer = []
    arr=[0]* (N+2)
    d={}
    for i in range(N+2):
        d[i]=0
    d2={}
    for i in range(N+2):
        d2[i]=0
    for i in stages:
        d[i-1]+=1
        d2[i]+=1
    for i in range(1,N+1):
        tmp=0
        for j in range(i,N+1):
            tmp+=d[j]
        if tmp+d2[i]!=0:
            arr[i]=d2[i]/(tmp+d2[i])
        else:
            arr[i]=0
    
    answer=[i for i in range(1,N+1)]
    print(arr)
    answer.sort(key=lambda a: [-arr[a],a])
    return answer