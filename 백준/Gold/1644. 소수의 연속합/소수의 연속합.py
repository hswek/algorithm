import sys
from collections import deque
import heapq
import math
n=int(input())
if n==1:
    print(0)
else:
    arr=[True]*(n+1)
    for i in range(2,int(math.sqrt(n+1)+1)):
        if arr[i]==True:
            j=2
            
            while(i*j<n+1):
                #print(i*j)
                arr[i*j]=False
                #print(i*j)
                j+=1
    prime=[]
    for i in range(2,n+1):
        if arr[i]==True:
            prime.append(i)
    l=len(prime)
    sum_prime=[0]*len(prime)
    sum_prime[0]=prime[0]
    result=0
    end=-1
    for i in range(1,l):
        sum_prime[i]=sum_prime[i-1]+prime[i]
        if end==-1 and  sum_prime[i]>=n:
            end=i
    if sum_prime[0]>=n:
        end=0
    start=-1
    #print(prime)
    #print(sum_prime)
    while(end!=l):
        if start==-1:
            if sum_prime[end]==n:
                result+=1
            start=0
            while end!=l and sum_prime[end]-sum_prime[start]<n:
                end+=1
            #print(end)
            if end==l:
                break

        while(sum_prime[end]-sum_prime[start]>=n):
            #print(start)
            start+=1
            if start==end:
                break 

        start-=1
        #print(start,end)
        if sum_prime[end]-sum_prime[start]==n:
            result+=1
        end+=1
    print(result)
        