def find_parent(x):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x])
    return parent[x]
def union(a,b):
    a=find_parent(a)
    b=find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
n=int(input())
parent=[0]*(n+1)
for i in range(1,n):
    parent[i]=i
x_arr=[]
y_arr=[]
z_arr=[]
edge=[]
for i in range(n):
    x,y,z=map(int,input().split())
    x_arr.append((x,i))
    y_arr.append((y,i))
    z_arr.append((z,i))
x_arr.sort()
y_arr.sort()
z_arr.sort()
for i in range(len(x_arr)-1):
    edge.append((x_arr[i+1][0]-x_arr[i][0],x_arr[i+1][1],x_arr[i][1]))
    edge.append((y_arr[i+1][0]-y_arr[i][0],y_arr[i+1][1],y_arr[i][1]))
    edge.append((z_arr[i+1][0]-z_arr[i][0],z_arr[i+1][1],z_arr[i][1]))
edge.sort()
result=0
now=0
for e in edge:
    weight,a,b=e[0],e[1],e[2]
    a_p=find_parent(a)
    b_p=find_parent(b)
    if a_p==b_p:
        continue
    else:
        union(a,b)
        result+=weight
        now+=1
    if now==n-1:
        break
print(result)