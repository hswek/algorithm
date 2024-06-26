import heapq
def solution(n, cores):

    answer = 0
    start=0
    end=999999999
    while start+1<end:
        mid=(start+end)//2
        tmp=0
        for core in cores:
            tmp+=(mid//core+1)
        if tmp>=n:
            end=mid
        else:
            start=mid
    tmp=0
    time=start+1
    for c in cores:
        tmp+=((time-1)//c)+1
    #print(tmp)
    for c in range(len(cores)):
        if time%cores[c]==0:
            tmp+=1
            if tmp==n:
                return c+1
    #print(start+1)
    return answer