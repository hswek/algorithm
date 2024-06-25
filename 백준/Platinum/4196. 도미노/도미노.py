import sys
from collections import deque
import heapq
import math
sys.setrecursionlimit(10**5)
#t=int(sys.stdin.readline().rstrip())
#n,k=map(int,sys.stdin.readline().rstrip().split())
#arr=[-1]+list(map(int,sys.stdin.readline().rstrip().split()))
#n,m=map(int,sys.stdin.readline().rstrip().split())
t=int(sys.stdin.readline().rstrip())
for _ in range(t):

	v,e=map(int,sys.stdin.readline().rstrip().split())
	arr=[[] for i in range(v)]
	for __ in range(e):
		i,j=map(int,sys.stdin.readline().rstrip().split())
		i-=1
		j-=1
		arr[i].append(j)
	q=deque()
	dfs_counter=0
	scc_id=[-1]*v
	visit=[-1]*v
	scc_counter=0
	def dfs(root):
		global q,dfs_counter,scc_id,scc_counter
		dfs_counter+=1
		visit[root]=dfs_counter
		m=dfs_counter
		q.append(root)
		for i in arr[root]:
			if visit[i]==-1:
				m=min(m,dfs(i))
			elif scc_id[i]==-1:
				m=min(m,visit[i])
		
		if m==visit[root]:
			while True:
				top=q.pop()
				scc_id[top]=scc_counter
				if top==root:
					break
			scc_counter+=1
		return m
	for i in range(v):
		if visit[i]==-1:
			dfs(i)
	in_degree=[0]*scc_counter
	for i in range(v):
		for j in arr[i]:
			if scc_id[i]!=scc_id[j]:
				in_degree[scc_id[j]]+=1
	result=0
	for i in range(scc_counter):
		if in_degree[i]==0:
			result+=1
	print(result)
		