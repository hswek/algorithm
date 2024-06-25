import sys
from collections import deque
d={}
n=int(sys.stdin.readline().rstrip())
for i in range(n-1):
	start,end=map(int,sys.stdin.readline().rstrip().split())
	if start in d:
		d[start].append(end)
	else:
		d[start]=[end]
	if end in d:
		d[end].append(start)
	else:
		d[end]=[start]
q=deque()
q.append(1)
arr=[-1] * (n+1)
arr[1]=1
while len(q)!=0:
	top=q.popleft()
	if top not in d:
		continue
	for i in d[top]:
		if arr[i]==-1:
			q.append(i)
			arr[i]=top
for i in range(2,n+1):
	print(arr[i])
	
	