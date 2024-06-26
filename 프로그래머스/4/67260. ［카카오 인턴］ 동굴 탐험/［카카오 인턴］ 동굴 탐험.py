
def solution(n, path, order):
    answer = True
    child=[[] for i in range(n)]
    for start,end in path:
        child[start].append(end)
        child[end].append(start)
    next_go={}
    can_not_go={}
    can_go=[0]*n
    for i in range(n):
        next_go[i]=[]
    for start,end in order:
        if end==0:
            return False
        next_go[start].append(end)
        can_not_go[end]=True
        can_go[end]+=1
    candidate=[0]
    now=0
    visit_num=0
    visit={}
    can_not_go_and_visit={}
    while len(candidate): 
        now=candidate.pop()
        #print(now,candidate,visit,can_not_go)
        if now in visit:
            continue
        visit[now]=True
        for c in next_go[now]:
            can_go[c]-=1
            if can_go[c]==0:
                del can_not_go[c]
                if c in can_not_go_and_visit:
                    candidate.append(c)
        for node in child[now]:
            if node in can_not_go:
                can_not_go_and_visit[node]=True
                continue
            if node not in visit:
                candidate.append(node)

    if len(visit)!=n:
        return False
    return answer