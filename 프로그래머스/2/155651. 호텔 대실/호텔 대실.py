import heapq
def solution(book_time):
    answer = 0
    arr=[]
    for start,end in book_time:
        start=int(start[:2])*60 + int(start[3:])
        end=int(end[:2])*60 + int(end[3:])+10
        arr.append([start,end])
    arr.sort()
    '''room=[]
    for start,end in arr:
        if len(room)!=0 and room[0]<=start:
            heapq.heappop(room)
        heapq.heappush(room,end)
    return len(room)'''
    m=1
    for i in range(len(arr)):
        tmp=1
        little_end=arr[i][1]
        for j in range(len(arr)):
            if i==j:
                continue
            #print(arr[j][0],arr[i][1])
            if arr[j][0]< arr[i][1] and arr[i][1]<=arr[j][1]:
                tmp+=1
            m=max(m,tmp)
    return m