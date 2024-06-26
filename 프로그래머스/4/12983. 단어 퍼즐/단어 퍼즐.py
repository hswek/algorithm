cache={}
def rec(i):
    global tri,s
    if i in cache:
        return cache[i]
    if len(s)==i:
        return 0
    now=tri
    result=99999999999
    for j in range(i,len(s)):
        w=s[j]
        if w not in now:
            cache[i]=result
            return result
        now=now[w]
        if "-1" in now:
            result=min(result,rec(j+1)+1)       
    cache[i]=result
    return result
import sys
sys.setrecursionlimit(10**6)
def solution(strs, t):
    global tri,s

    s=t
    answer = 0
    tri={} 
    for word in strs:
        now=tri
        l=len(word)
        for i,w in enumerate(word):
            if w not in now:
                now[w]={} 
            now=now[w]
        
        now["-1"]=True
    ans=rec(0)
    if ans==99999999999:
        return -1
    return ans