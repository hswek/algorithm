from collections import deque
def solution(n, edge):
    answer = 0
    d=deque([[0,0]])
    visit=[-1]*n
    visit[0]=1
    arr=[[] for i in range(n)]
    for i,j in edge:
        arr[i-1].append(j-1)
        arr[j-1].append(i-1)
    m=0
    answer=[]
    while len(d):
        now,l=d.popleft()
        #print(now,l)
        if m<l:
            m=l
            answer=[]
            answer.append(now)
        else:
            answer.append(now)
        for i in arr[now]:
            if visit[i]==-1:
                d.append([i,l+1])
                visit[i]=1
    return len(answer)