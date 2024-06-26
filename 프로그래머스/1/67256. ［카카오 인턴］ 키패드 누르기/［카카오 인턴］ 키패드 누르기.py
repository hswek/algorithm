def solution(numbers, hand):
    answer = ''
    arr=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left=[3,0]
    right=[3,2]
    arr2={}
    for i in range(4):
        for j in range(3):
            arr2[arr[i][j]]=[i,j]
    for num in numbers:
        #print(left,right)
        pos=arr2[num]
        l=abs(pos[0]-left[0]) + abs(pos[1]-left[1])
        r=abs(pos[0]-right[0]) + abs(pos[1]-right[1])
        if num in [1,4,7]: 
            answer+='L'
            left=pos
        elif num in [3,6,9]: 
            answer+='R'
            right=pos
        elif l>r:
            answer+='R'
            right=pos
        elif l<r:
            answer+='L'
            left=pos
        elif l==r and hand=='left':
            answer+='L'
            left=pos
        elif l==r and hand=='right':
            answer+='R'
            right=pos
    return answer
