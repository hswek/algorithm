import sys
def dfs(d,travel,start):
    global answer,nn
    if len(travel)==nn:
        answer.append(travel.copy())
        return
    if start not in d:
        return
    for nex in list(d[start].keys()):
        if d[start][nex]==0:
            continue
        d[start][nex]-=1
        travel.append(nex)
        dfs(d,travel,nex)
        travel.pop()
        d[start][nex]+=1
    return

def solution(tickets):
    sys.setrecursionlimit(10**7)
    global answer,nn
    nn=len(tickets)+1
    answer = []
    start='ICN'
    d={}
    for s,e in tickets:
        if s not in d:
            d[s]={e:1}
        elif e not in d[s]:
            d[s][e]=1
        else:
            d[s][e]+=1
    tmp=[]
    tmp.append(start)
    dfs(d,tmp,start)
    #
    #print(answer)
    answer.sort()
    if len(answer):
        return answer[0]
    return 1