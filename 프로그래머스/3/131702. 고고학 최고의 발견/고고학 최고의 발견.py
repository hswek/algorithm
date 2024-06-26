import copy
def get_greedy(start,clocks):
    c=copy.deepcopy(clocks)
    result=0
    for i in range(len(clocks)):
        c[0][i]=(c[0][i]+start[i])%4
        if i>=1:
            c[0][i-1]=(c[0][i-1]+start[i])%4
        if i!=len(clocks)-1:
            c[0][i+1]=(c[0][i+1]+start[i])%4
        c[1][i]=(c[1][i]+start[i])%4
        result+=start[i]
    for i in range(1,len(clocks)):
        for j in range(len(clocks)):
            if c[i-1][j]!=0:
                h=4-c[i-1][j]
                result+=h
                c[i-1][j]=0
                c[i][j]=(c[i][j]+h)%4
                if j>=1:
                    c[i][j-1]=(c[i][j-1]+h)%4
                if j!=len(clocks)-1:
                    c[i][j+1]=(c[i][j+1]+h)%4
                if i!=len(clocks)-1:
                    c[i+1][j]=(c[i+1][j]+h)%4
    for j in range(len(clocks)):
        if c[-1][j]!=0:
            return 9999999999999999
    print(result)
    return result
def dfs(idx,l,start,clocks):
    global answer
    if idx==l:
        #print(start)
        result=get_greedy(start,clocks)
        answer=min(result,answer)
        return
    for i in range(4):
        start[idx]=i
        dfs(idx+1,l,start,clocks)
def solution(clocks):
    global answer
    answer = 9999999999999999999
    dfs(0,len(clocks),[0]*len(clocks),clocks)
    return answer