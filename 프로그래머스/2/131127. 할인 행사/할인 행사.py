from collections import deque
def arr_same(arr1,arr2):
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            return False
    return True
def solution(want, number, discount):
    answer = 0
    arr1=[]
    for i in range(len(want)):
        for j in range(number[i]):
            arr1.append(want[i])
    arr1.sort()

    for i in range(len(discount)-9):
        arr2=discount[i:i+10]
        arr2.sort()
        if arr_same(arr1,arr2)==True:
            #print(i)
            answer+=1
    return answer
