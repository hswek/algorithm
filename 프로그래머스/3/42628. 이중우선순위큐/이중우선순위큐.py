import heapq
def solution(operations):
    answer = []
    max_heap=[]
    min_heap=[]
    idx=0
    dic={}
    for o in operations:
        a,b=o.split()
        if a=='I':
            heapq.heappush(max_heap,[-int(b),idx])
            heapq.heappush(min_heap,[int(b),idx])
            idx+=1
        if a=='D' and b=='1':
            is_pop=False
            while len(max_heap):
                c,d=heapq.heappop(max_heap)
                if d not in dic:
                    is_pop=True
                    break
            if is_pop==True:
                dic[d]=True
        if a=='D' and b=='-1':
            is_pop=False
            while len(min_heap):
                c,d=heapq.heappop(min_heap)
                if d not in dic:
                    is_pop=True
                    break
            if is_pop==True:
                dic[d]=True
    #print(max_heap)
    #print(min_heap)
    #print(dic)
    is_pop=False
    result_max=-999999999999999999999999
    result_min=-999999999999999999999999
    while len(max_heap):
        c,d=max_heap[0]
        if d not in dic:
            result_max=-c
            break
        else:
            heapq.heappop(max_heap)
    while len(min_heap):
        c,d=min_heap[0]
        if d not in dic:
            result_min=c
            break
        else:
            heapq.heappop(min_heap)
    if result_max==-999999999999999999999999:
        return [0,0]
    else:
        return [result_max,result_min]
        
    return answer