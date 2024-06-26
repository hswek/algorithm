far_arr=[]
def find_far_node(node,n,visit):
    global far_node,max_num,arr
    visit[node]=True
    far_arr.append(n)
    if n>max_num:
        max_num=n
        far_node=node
    for child in arr[node]:
        if child not in visit:
            find_far_node(child,n+1,visit)
cache={}
import sys
sys.setrecursionlimit(10**6)
def find_distance(root,node2,visit):
    cache_str=str(root)+"_"+str(node2)
    if cache_str in cache:
        return cache[cache_str]
    visit[root]=True
    if root==node2:
        return 0
    global arr
    result=9999999999999999
    for child in arr[root]:
        if child not in visit:
            result=find_distance(child,node2,visit)
            if result<=9999999999999:
                cache[cache_str]=result+1
                return result+1
    cache[cache_str]=9999999999999999
    return 9999999999999999
def solution(n, edges):
    answer = 0
    head=1
    global arr
    arr=[[] for _ in range(n+1)]
    for start,end in edges:
        arr[start].append(end)
        arr[end].append(start)
    global far_node,max_num
    far_node=-1
    max_num=-1
    find_far_node(1,0,{})
    node1=far_node
    far_node=-1
    max_num=-1
    global far_arr
    far_arr=[]
    find_far_node(node1,0,{})
    far_arr.sort()
    if far_arr[-2]==far_arr[-1]:
        return far_arr[-1]

    tmp=far_arr[-2]
    far_arr=[]
    find_far_node(far_node,0,{})
    far_arr.sort()
    return far_arr[-2]