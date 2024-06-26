
def solution(n):
    answer = 0
    arr=[0,1,0]
    for i in range(2,n+1):
        arr[i%3]=arr[(i+2)%3]+arr[(i+1)%3]
    return arr[n%3]%1234567
    return answer