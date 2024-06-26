def fall(now_node,value):
    if len(arr[now_node])==1:
        sum_arr[now_node]+=value
        return
    fall(arr[now_node][arr[now_node][-1]],value)
    if arr[now_node][-1]==len(arr[now_node])-2:
        arr[now_node][-1]=0
    else:
        arr[now_node][-1]+=1
def get_fall_node(now_node):
    if len(arr[now_node])==1:
        return now_node
    return get_fall_node(arr[now_node][arr[now_node][-1]])
    
def solution(edges, target):
    answer = []
    global arr
    global sum_arr
    max_node=0
    for start,end in edges:
        max_node=max([max_node,start,end])
    arr=[[] for i in range(max_node+1)]
    sum_arr=[0]*(max_node+1)
    count_fall=[0]*(max_node+1)
    for start,end in edges:
        arr[start].append(end)
    for edge in arr:
        edge.sort()
        if len(edge)!=0:
            edge.append(0)
        else:
            edge.append(-1)
    head=1
    target.insert(0,0)
    fall_seq=[]
    def all_node_can_get(count_fall,target):
        for i in range(1,max_node+1):
            if not (count_fall[i]*3>=target[i] and target[i]>=count_fall[i]):
                return False
        return True
    while True:
        fall_node=get_fall_node(head)
        if count_fall[fall_node]==target[fall_node]:
            return [-1]
        count_fall[fall_node]+=1
        fall_seq.append(fall_node)
        fall(head,0)
        if all_node_can_get(count_fall,target):
            break
    d={}
    for i in range(1,max_node+1):
        d[i]=[]
        d[i].extend([3]*((target[i]-count_fall[i])//2))
        d[i].extend([2]*((target[i]-count_fall[i])%2))
        d[i].extend([1]*(count_fall[i]-len(d[i])))
    for what_node in fall_seq:
        answer.append(d[what_node][-1])
        d[what_node].pop()
                    
    return answer