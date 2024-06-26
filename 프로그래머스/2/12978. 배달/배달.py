import heapq
def solution(N, road, K):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')
    h=[[0,1]]
    visit=[-1]*(N+1)
    arr=[[9999999]*(N+1) for i in range(N+1)]
    for i,j,w in road:
        arr[i][j]=min(arr[i][j],w)
        arr[j][i]=min(arr[j][i],w)
    answer=[-1]*(N+1)
    while len(h):
        dis,now=heapq.heappop(h)
        if visit[now]!=-1:
            continue
        #print(dis,now)
        visit[now]=True
        answer[now]=dis
        for i in range(N+1):
            if arr[now][i]==9999999 or visit[i]!=-1:
                continue
            heapq.heappush(h,[dis+arr[now][i],i])
    result=0
    #print(answer)
    for i in answer:
        if i!=-1 and i<=K:
            result+=1
    return result