import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**5)
n=int(sys.stdin.readline().rstrip())
d={}
for i in range(n):
	start,end1,end2=sys.stdin.readline().rstrip().split()
	d[start]=[]
	if end1!='.':
		d[start].append([1,end1])
	if end2!='.':
		d[start].append([2,end2])
def recursive1(root):
	print(root,end='')
	for i in d[root]:	
		recursive1(i[1])
def recursive2(root):
	if len(d[root])==0:
		print(root,end='')
		return
	if len(d[root])==1:
		if d[root][0][0]==1:
			recursive2(d[root][0][1])
			print(root,end='')
			return
		else:
			print(root,end='')
			recursive2(d[root][0][1])

			return
			
	if len(d[root])==2:
		recursive2(d[root][0][1])
		print(root,end='')
		recursive2(d[root][1][1])
		return
def recursive3(root):
	if len(d[root])==0:
		print(root,end='')
		return
	if len(d[root])==1:
		recursive3(d[root][0][1])
		print(root,end='')
	
	
	if len(d[root])==2:
		recursive3(d[root][0][1])
		recursive3(d[root][1][1])
		print(root,end='')
		
		return
	
	
recursive1('A')
print()
recursive2('A')
print()
recursive3('A')
