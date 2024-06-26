from collections import deque
def get_child(root,visit,child,n): 
    visit[root]=1
    answer=1
    for c in range(1,n+1):
        if child[root][c]==1 and visit[c]==-1:
            answer+=get_child(c,visit,child,n)
    return answer
        
    
def solution(n, wires):
    answer = -1
    root=1
    child=[[-1] * (n+1) for i in range(n+1)]
    for wire in wires:
        child[wire[0]][wire[1]]=1
        child[wire[1]][wire[0]]=1
    m=13311331313313131
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i==j:
                continue
            if child[i][j]==1:
                child[i][j]=0
                child[j][i]=0
                visit=[-1] * (n+1) 
                a=get_child(i,visit,child,n)
                visit=[-1] * (n+1) 
                b=get_child(j,visit,child,n)
                m=min(m,abs(a-b))
                child[i][j]=1
                child[j][i]=1
    return m