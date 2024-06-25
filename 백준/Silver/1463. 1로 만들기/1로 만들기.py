#x,y,z=map(int,input().split())
import sys
n=int(input())
cal_list=[99]*(n+1)
cal_list[1]=0
for i in range(2,n+1):
    x1=1000
    x2=1000
    x3=cal_list[i-1]+1
    if i%3==0:
        x1=cal_list[i//3]+1
    if i%2==0:
        x2=cal_list[i//2]+1
    cal_list[i]=min([x1,x2,x3])
    #print(i,cal_list[i])
    if i==n:
        break
print(cal_list[n])