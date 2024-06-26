def solution(n, times):
    answer = 0
    end=9999999999999999
    start=0
    while True:
        if start+1==end:
            break
        mid=(start+end)//2
        tmp=0
        for t in times:
            tmp+=(mid//t)
        print(mid,tmp)
        if tmp>=n:
            end=mid
        else:
            start=mid
    #print(start)
    return end