def solution(n):
    answer = 0
    arr=[]
    while n!=0:
        arr.append(n%3)
        n=n//3
    arr.reverse()
    #print(arr)
    for i in range(len(arr)-1,-1,-1):
        answer+=3**i*arr[i]
        
    return answer