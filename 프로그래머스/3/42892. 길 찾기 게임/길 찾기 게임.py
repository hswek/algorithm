from collections import deque
def prev_rec(idx,arr,tmp):
    left,right=arr[idx]
    tmp.append(idx)
    if left!=-1:
        prev_rec(left,arr,tmp)
    if right!=-1:
        prev_rec(right,arr,tmp)
def later_rec(idx,arr,tmp):
    left,right=arr[idx]
    if left!=-1:
        later_rec(left,arr,tmp)
    if right!=-1:
        later_rec(right,arr,tmp)
    tmp.append(idx)
import sys
def solution(nodeinfo):
    sys.setrecursionlimit(10**6)
    answer = [[]]
    arr=[[-1,-1] for i in range(len(nodeinfo)+1000)]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x:[-x[1],x[0]])
    q=deque([[nodeinfo[0][2],nodeinfo[0][0],nodeinfo[0][1],-1,999999999999,0]])
    while len(q):        
        idx,middle,ny,lx,rx,z=q.popleft()
        depth=-1
        for i in range(z+1,len(nodeinfo)):
            if depth==-1 and nodeinfo[i][1]<ny:
                depth=nodeinfo[i][1]
            if depth!=-1:
                if nodeinfo[i][1]==depth:
                    if nodeinfo[i][0]>lx and nodeinfo[i][0]<middle:
                        arr[idx][0]=nodeinfo[i][2]
                        q.append([nodeinfo[i][2],nodeinfo[i][0],nodeinfo[i][1],lx,middle,i])
                    elif nodeinfo[i][0]>middle and nodeinfo[i][0]<rx:
                        arr[idx][1]=nodeinfo[i][2]
                        q.append([nodeinfo[i][2],nodeinfo[i][0],nodeinfo[i][1],middle,rx,i])
                else:
                    break
    a=[]
    b=[]
    prev_rec(nodeinfo[0][2],arr,a)
    later_rec(nodeinfo[0][2],arr,b)
    return [a,b]