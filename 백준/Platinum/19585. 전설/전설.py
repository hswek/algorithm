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
        self.root={'*':False}
    def insert(self,s):
        cur_node=self.root
        for c in s:
            if c not in cur_node:
                cur_node[c]={'*':False}    
            cur_node=cur_node[c]
        cur_node['*']=True
    def search(self,s):
        global name
        cur_node=self.root
        idx=0
        arr={}
        for c in s[:-1]:
            idx+=1
            if c not in cur_node:
                return arr
            cur_node=cur_node[c]
            if cur_node['*']==True:
                if s[idx:] in name:
                    return True
        return False
n,m=map(int,sys.stdin.readline().rstrip().split())
color=trie_node()
#name=trie_node()
name={}
for _ in range(n):
    s=sys.stdin.readline().rstrip()
    color.insert(s)
for _ in range(m):
    s=sys.stdin.readline().rstrip()
    name[s]=True
    #name.insert(s[::-1])
def is_True(s,arr1,arr2):
    for i in arr1.keys():
        if len(s)-i in arr2.keys():
            return True
    return False
t=int(sys.stdin.readline().rstrip())
for i in range(t):
    s=sys.stdin.readline().rstrip()
    a=color.search(s)
    #arr2=name.search(s[::-1])

    if a==True:
        print('Yes')
    else:
        print('No')
