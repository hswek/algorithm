def rec(info,node,sheep,wolf,can_go):
    global ans
    #print(node,sheep,wolf,can_go)
    ans=max(ans,sheep)
    result=0
    for i in parent[node]:
        #print(i)
        can_go.append(i)
    for i in range(len(can_go)):
        tmp=can_go[i]
        ns=sheep
        nw=wolf
        if info[tmp]==0:
            ns+=1
        else:
            nw+=1
        if nw>=ns:
            continue
        next_arr=can_go.copy()
        next_arr.pop(i)
        rec(info,tmp,ns,nw,next_arr)
        
def solution(info, edges):
    global ans,parent
    ans = 0
    l=len(info)
    parent=[[] for i in range(l+1)]
    for i,j in edges:
        parent[i].append(j)
    rec(info,0,1,0,[])
    return ans