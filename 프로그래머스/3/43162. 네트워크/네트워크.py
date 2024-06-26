def dfs(i,computers):
    visit[i]=1
    for j in range(len(computers)):
        if i==j:
            continue
        if computers[i][j]==1 and visit[j]==-1:
            dfs(j,computers)
    
def solution(n, computers):
    answer = 0
    global visit
    visit=[-1]* len(computers[0])
    for i in range(len(computers)):
        if visit[i]==-1:     
            answer+=1
            dfs(i,computers)
    return answer