import sys
import heapq
import copy
import math
def get_sqr_list(num):
    arr=[]
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            arr.append(i)
    new_arr=[]
    for i in arr:
        if i*i!=num:
            new_arr.append(num//i)
    new_arr.reverse()
    arr.extend(new_arr)
    return arr
def get_ans(s):
    sqr_list=get_sqr_list(len(s))
    ans=1
    for i in sqr_list:
        repeat=s[:i]
        how_repeat=len(s)//i
        result=True
        for j in range(how_repeat):
            na=s[j*i:i+j*i]
            if na!=repeat:
                result=False
                break
        if result==True:
            return how_repeat
                
for i in range(10):
    s=sys.stdin.readline().rstrip()
    if s=='.':
        break
    print(get_ans(s))

    