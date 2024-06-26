from collections import deque
def solution(gems):
    answer = []
    g=[]
    for i in gems:
        g.append(str(i))
    what_to_get=len(set(g))
    r=9999999
    prev_len=0
    tmp=deque([])
    start=0
    now_d={}
    for end in range(len(g)):
        tmp.append(g[end])
        if g[end] in now_d:
            now_d[g[end]]+=1
        else:
            now_d[g[end]]=1
        if what_to_get==len(now_d):
            if r>len(tmp):
                r=len(tmp)
                answer=[start+1,end+1]
            while what_to_get==len(now_d):
                if r>len(tmp):
                    r=len(tmp)
                    answer=[start+1,end+1]
                now_d[tmp[0]]-=1
                if now_d[tmp[0]]==0:
                    del now_d[tmp[0]]
                start+=1
                tmp.popleft()
    return answer