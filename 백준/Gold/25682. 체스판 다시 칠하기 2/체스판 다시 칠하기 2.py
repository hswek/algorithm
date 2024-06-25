import sys
n,m,k=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
def cal_sum(color):
    global n,m,k
    sum_arr=[[0]*(m+1) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if (i+j)%2==0:
                if arr[i][j]==color:
                    v=0
                else:
                    v=1
            else:
                if arr[i][j]==color:
                    v=1
                else:
                    v=0
            
            sum_arr[i+1][j+1]=sum_arr[i][j+1]+sum_arr[i+1][j]-sum_arr[i][j]+v
    min_num=987654321
    #print(sum_arr)
    for i in range(0,n+1-k):
        for j in range(0,m+1-k):  
            result=sum_arr[i+k][j+k]-sum_arr[i+k][j]-sum_arr[i][j+k]+sum_arr[i][j]
            min_num=min(min_num,result)
    return min_num
print(min(cal_sum('B'),cal_sum('W')))