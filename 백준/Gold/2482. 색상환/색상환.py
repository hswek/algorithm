import sys
#a,b=sys.stdin.readline().rstrip().split()
n=int(input())
k=int(input())
cache=[[[[-1]* (k+1) for z in range(2)]  for i in range(2)] for i in range(n)]
def recursvie(start,start_color,prev_color,color_num):
    global k
    #print(start,start_color,prev_color,color_num)
    if color_num==k:
        return 1
    if start==n:
        return 0
    if cache[start][start_color][prev_color][color_num]!=-1:
        return cache[start][start_color][prev_color][color_num]
    m=0
    if prev_color==0:
        if start==n-1 and start_color==1:
            m+=recursvie(start+1,start_color,0,color_num)
        else:
            m+=recursvie(start+1,start_color,0,color_num)
            m+=recursvie(start+1,start_color,1,color_num+1)
        
    elif prev_color==1:
        m+=recursvie(start+1,start_color,0,color_num)

    cache[start][start_color][prev_color][color_num]=m
    return m
    
    
m=0
for i in range(2):
    m+=recursvie(1,i,i,i)%1000000003
print(m%1000000003)