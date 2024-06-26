import math
def solution(arr):
    answer = 0
    n=1
    for i in arr:
        n= n*i// math.gcd(i,n)
    return n