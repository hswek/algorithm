def get_col(arr,i):
    tmp=[]
    for j in range(len(arr)):
        tmp.append(arr[j][i])
    return tmp
    
def a(tmp1,tmp2):
    tmp=0
    for i in range(len(tmp1)):
        tmp=tmp+tmp1[i]*tmp2[i]
    return tmp
def solution(arr1, arr2):
    
    answer = [[0]* len(arr2[0]) for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            #print(a(arr1[i],get_col(arr2,j)))
            answer[i][j]=a(arr1[i],get_col(arr2,j))
            
    return answer