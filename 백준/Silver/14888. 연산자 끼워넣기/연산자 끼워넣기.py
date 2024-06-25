max_num=-2000000000
import sys
min_num=2000000000
n=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr2=list(map(int,sys.stdin.readline().rstrip().split()))
cal_arr=[]
def cal(cal_arr):
    global max_num,min_num
    #print(cal_arr)
    r=arr[0]
    for i in range(len(cal_arr)):
        if cal_arr[i]==0:
            r+=arr[i+1]
        if cal_arr[i]==1:
            r-=arr[i+1]
        if cal_arr[i]==2:
            r*=arr[i+1]
        if cal_arr[i]==3:
            if r<0:
                r=-r
                r=r//arr[i+1]
                r=-r
            else:
                r=r//arr[i+1]
    max_num=max(max_num,r)
    min_num=min(min_num,r)
def arr_cal(cal_arr,a):
    if n-1==a:
        cal(cal_arr)    
    for i in range(4):
        if arr2[i]!=0:
            cal_arr.append(i)
            arr2[i]-=1
            arr_cal(cal_arr,a+1)
            cal_arr.pop()
            arr2[i]+=1
arr_cal(cal_arr,0)
print(max_num,min_num)