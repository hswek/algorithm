def to_bi(num):
    arr=[]
    while num!=0:
        arr.append(num%2)
        num=num//2
    arr.reverse()
    return arr
def get_l(l):
    tmp=1
    while True:
        if l<=2**tmp-1 and l>2**(tmp-1)-1:
            break
        tmp+=1
    return tmp
def to_int(arr):
    arr.reverse()
    result=0
    for i in range(len(arr)):
        if arr[i]==1:
            result+=2**i
    arr.reverse()
    return result
def can(arr):
    if len(arr)<=1:
        return True
    left=arr[:len(arr)//2]
    right=arr[len(arr)//2+1:]
    mid=arr[len(arr)//2]
    l=to_int(left)
    r=to_int(right)
    if (l!=0 or r!=0) and mid==0:
        return False
    tmp=0
    if can(left)==False or can(right)==False:
        return False
    return True
def solution(numbers):
    answer = []
    for num in numbers:
        bin_arr=to_bi(num)
        l=get_l(len(bin_arr))
        n=2**l-1
        arr=[0]*n
        for i in range(len(bin_arr)):
            arr[i-len(bin_arr)]=bin_arr[i]
        if can(arr)==True:
            answer.append(1)
        else:
            answer.append(0)
    return answer