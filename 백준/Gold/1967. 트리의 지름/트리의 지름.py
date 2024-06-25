import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n=int(sys.stdin.readline().rstrip())
arr=[[] for i in range(n+1)]
for i in range(n-1):
	start,end,weight=map(int,sys.stdin.readline().rstrip().split())
	arr[start].append([end,weight])
def recursive(start):
	#print(start)
	depth=0
	length=0
	depth_arr=[]
	for child,weight in arr[start]:
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