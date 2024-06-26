
def solution(priorities, location):
    d={}
    answer = 0
    for i in priorities:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    arr=d.items()
    arr=map(list,arr)
    arr=list(arr)
    arr.sort()
    print(arr)
    idx=0
    while True:
        if priorities[idx]==-1 or arr[-1][0] > priorities[idx]:
            idx+=1
            idx=idx%len(priorities)
            continue
        else:
            answer+=1
            if idx==location:
                break
            arr[-1][1]-=1
            if arr[-1][1]==0:
                arr.pop(-1)
            priorities[idx]=-1
            idx+=1
            idx=idx%len(priorities)
        
            
    return answer