def solution(n, arr1, arr2):
    answer = []
    l=len(arr1)
    for i in range(len(arr1)):
        tmp=arr1[i] | arr2[i]
        #print(tmp)
        tmp_arr=[]
        for j in range(l):
            tmp_arr.append(tmp%(2))
            tmp=tmp//2
        tmp_arr.reverse()
        s=''
        for z in tmp_arr:
            if z==0:
                s=s+' '
            else:
                s=s+'#'
        
        answer.append(s)
    return answer