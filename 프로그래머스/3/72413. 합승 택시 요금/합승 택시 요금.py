import heapq
def solution(n, s, a, b, fares):
    answer =11111111111110
    visit=[-1]*(n+1)
    arr=[[] for i in range(n+1)]

    arr=[[9999999999]*(n+1) for i in range(n+1)]
    for i,j,z in fares:
        arr[i][j]=z
        arr[j][i]=z
    for i in range(1,n+1):
        arr[i][i]=0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if arr[i][k]+arr[k][j]<=arr[i][j]:
                    arr[i][j]=arr[i][k]+arr[k][j]
    answer=arr[s][a]+arr[s][b]
    for i in range(1,n+1):
        #print(i,arr[s][n],arr[n][a],arr[n][b])
        tmp=arr[s][i]+arr[i][a]+arr[i][b]
        answer=min(tmp,answer)
    return answer