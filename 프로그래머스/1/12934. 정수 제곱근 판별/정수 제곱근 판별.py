import math
def solution(n):
    answer = 0
    if int(math.sqrt(n))==math.sqrt(n):
        return (math.sqrt(n)+1)**2
    return -1