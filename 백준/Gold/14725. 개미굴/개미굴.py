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
        for c in s:
            if c not in cur_node:
                return False
            cur_node=cur_node[c]
        return '*' in cur_node
    def dfs(self,depth,root):
        #print(root)
        arr=list(root.keys())
        arr.sort()
        for i in arr:
            if i=='*':
                continue
            print('--'*depth,end='')
            print(i)
            self.dfs(depth+1,root[i]) 
        
n=int(sys.stdin.readline().rstrip())
root=trie_node()
for _ in range(n):
    s=sys.stdin.readline().rstrip()[2:]
    s=s.split()
    root.insert(s)
root.dfs(0,root.root)
    