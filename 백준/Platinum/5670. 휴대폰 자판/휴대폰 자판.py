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
        self.root={}
    def insert(self,s):
        cur_node=self.root
        for c in s:
            if c not in cur_node:
                cur_node[c]={}
            cur_node=cur_node[c]
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
    def dfs(self,depth,root,is_start):
        global r
        for c in root.keys():
            #print(c)
            if '*'==c:
                r+=depth
            else:
                if is_start==False and len(root)==1:
                    self.dfs(depth,root[c],False)
                else:
                    self.dfs(depth+1,root[c],False)
while True:
    try:
        n=int(sys.stdin.readline().rstrip())
    except:
        exit()
    root=trie_node()
    arr=[]
    for _ in range(n):
        s=sys.stdin.readline().rstrip()
        arr.append(s)
        root.insert(s)
    r=0
    #print(root.root)
    root.dfs(0,root.root,True)
    print('%.2f'%(r/len(arr)))

