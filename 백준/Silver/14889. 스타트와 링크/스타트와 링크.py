
import sys
n=int(input())
score_arr=[]
for i in range(n):
    score_arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
used=[0]*30
result=9876543421
#1부터 n까지 m개 뽑기 
def cal_result(arr):
    global result
    arr2=[]
    tmp=0
    for i in range(1,n+1):
        if i not in arr:
            arr2.append(i)
    
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i in arr and j in arr:
                tmp+=score_arr[i-1][j-1]
                tmp+=score_arr[j-1][i-1]
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i in arr2 and j in arr2:
                tmp-=score_arr[i-1][j-1]
                tmp-=score_arr[j-1][i-1]
    #print(arr,arr2,tmp)
    result=min(result,abs(tmp))
def comb(comb_arr,n,m,idx):
    if m==0:
        cal_result(comb_arr)
    for i in range(idx,n+1):
        comb_arr.append(i)
        comb(comb_arr,n,m-1,i+1)
        comb_arr.pop()
comb_arr=[]
comb(comb_arr,n,n//2,1)
print(result)