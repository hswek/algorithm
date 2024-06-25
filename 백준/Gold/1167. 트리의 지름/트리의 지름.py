import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n=int(sys.stdin.readline().rstrip())
arr=[[] for i in range(n+1)]
child_arr=[[] for i in range(n+1)]
d={}
for i in range(n):
	tmp=list(map(int,sys.stdin.readline().rstrip().split()))
	start=tmp[0]
	num=(len(tmp)-2)//2
	for i in range(1,len(tmp)-1,2):
		end,weight=tmp[i],tmp[i+1]
		arr[start].append([end,weight])
q=deque()
q.append(1)
while(len(q)!=0):
	top=q.popleft()
	#print(top)
	for i,weight in arr[top]:
		#print(top,i)
		if len(child_arr[i])!=0:
			continue
		child_arr[top].append([i,weight])
		q.append(i)
#print(child_arr)

def recursive(start):
	#print(start)
	depth=0
	length=0
	depth_arr=[]
	for child,weight in child_arr[start]:
		#print(child)
		child_depth,child_length=recursive(child)
		length=max(length,child_length)
		depth_arr.append(child_depth+weight)
	depth_arr.sort(reverse=True)
	if len(depth_arr)==0:
		return 0,0
	if len(depth_arr)==1:
		return [depth_arr[0],max(depth_arr[0],length)]
	else:
		length=max(length,depth_arr[0]+depth_arr[1])
		return [depth_arr[0],length]
	
	
print(recursive(1)[1])