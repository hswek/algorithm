def find(i):
    global parent
    if parent[i]==i:
        return i
    parent[i]=find(parent[i])
    return parent[i]
def union(m1,m2):
    global parent
    parent[find(m1)]=find(m2)
def solution(n, costs):
    global parent
    answer = 0
    costs.sort(key=lambda x:x[2])
    parent=[ i for i in range(n)]
    for i,j,cost in costs:
        if find(i)!=find(j):
            union(i,j)
            #print(parent,find(i),find(j),cost)
            answer+=cost
            

    
    return answer