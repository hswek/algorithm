def solution(X, Y):
    answer = ''
    arr1=[0]*10
    arr2=[0]*10
    for i in X:
        arr1[int(i)]+=1
    for i in Y:
        arr2[int(i)]+=1
    for i in range(9,-1,-1):
        arr1[i]=min(arr1[i],arr2[i])
        answer+=str(i)*arr1[i]
    if answer!='' and answer[0]=='0':
        answer='0'
    if answer=='':
        answer='-1'
    return answer