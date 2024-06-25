import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(int(10**5))
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
#n,m=map(int,sys.stdin.readline().rstrip().split())
class trie_node:
    def __init__(self):
        self.root={'can_del':True}
    def insert(self,s):
        cur_node=self.root
        for c in s:
            if c not in cur_node:
                cur_node[c]={'can_del':True}
            cur_node=cur_node[c]
        cur_node['can_del']=True
        cur_node['*']=s

    def search(self,s):
        cur_node=self.root
        r=1
        a=0
        for c in s:
            if c not in cur_node:
                return len(s)
            if a!=0 and len(cur_node)>1:
                r+=1
            cur_node=cur_node[c]
            a=1
        return r
    def can_not_del(self,s):
        cur_node=self.root
        for c in s:
            cur_node['can_del']=False
            if c not in cur_node:
                return
            cur_node=cur_node[c]
        cur_node['can_del']=False
        return
    def del_all(self,root,s):
        global r
        #print(root)
        if root['can_del']==True:
            r+=1
            #print(s)
            return
        for i in root.keys():
            #print(i)
            if i=='can_del':
                continue
            if i=='*':
                #print(s+i)
                r+=1
                continue
            self.del_all(root[i],s+i)
        
t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    root=trie_node()
    for _ in range(n):
        s=sys.stdin.readline().rstrip()
        root.insert(s)
    m=int(sys.stdin.readline().rstrip())
    for _ in range(m):
        s=sys.stdin.readline().rstrip()
        root.can_not_del(s)
    r=0
    root.del_all(root.root,'')
    #print(root.root)
    print(r)
