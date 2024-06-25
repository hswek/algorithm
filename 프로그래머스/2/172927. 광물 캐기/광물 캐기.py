from itertools import permutations,combinations
def dfs(picks,minerals):
    global d
    #print(picks,minerals)
    cc=picks[0]*100+picks[1]*10+picks[2]
    if len(minerals)==0 or (picks[0]==0 and picks[1]==0 and picks[2]==0):
        return 0
    if cache[cc]!=-1:
        return cache[cc]
    a=98765432111
    b=98765432111
    c=98765432111
    if picks[0]!=0:
        tmp=0
        for i in range(min(5,len(minerals))):
            tmp+=d['diamond'][minerals[i]]
        picks[0]-=1
        a=tmp+dfs(picks,minerals[min(5,len(minerals)):])
        picks[0]+=1
    if picks[1]!=0:
        tmp=0
        for i in range(min(5,len(minerals))):
            tmp+=d['iron'][minerals[i]]
        picks[1]-=1
        b=tmp+dfs(picks,minerals[min(5,len(minerals)):])
        picks[1]+=1
    if picks[2]!=0:
        tmp=0
        for i in range(min(5,len(minerals))):
            tmp+=d['stone'][minerals[i]]
        picks[2]-=1
        c=tmp+dfs(picks,minerals[min(5,len(minerals)):])
        picks[2]+=1
    cache[cc]=min([a,b,c])
    return min([a,b,c])
def solution(picks, minerals):
    global d,cache
    cache=[-1]*1000
    d={'diamond':{'diamond':1,'iron':1,'stone':1},'iron':{"diamond":5,"iron":1,"stone":1},"stone":{"diamond":25,"iron":5,"stone":1}}
    return dfs(picks,minerals)