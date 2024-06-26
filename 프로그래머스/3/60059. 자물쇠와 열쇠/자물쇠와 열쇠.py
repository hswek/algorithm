import copy
def add(key,lock,i,j,n,m):
    tmp=copy.deepcopy(lock)
    for i2 in range(n):
        for j2 in range(n):
            tmp[i+i2][j+j2]+=key[i2][j2]

    for i2 in range(m,2*m):
        for j2 in range(m,2*m):
            if tmp[i2][j2]!=1:
                return False
    return True
def solution(key, lock):
    answer = True
    n,m=len(key),len(lock)
    new_key=[[0] *n for i in range(n)]
    key_arr=[key]
    for i in range(3):
        tmp=[[0] * n for i in range(n)]
        tmp_key=key_arr[-1]
        for j in range(n):
            for z in range(n):
                tmp[j][z]=tmp_key[n-1-z][j]
        key_arr.append(tmp)
    arr=[[0]*3*m for i in range(3*m)]
    for i in range(m,2*m):
        for j in range(m,2*m):
            arr[i][j]=lock[i-m][j-m]
    for i in range(2*m):
        for j in range(2*m):
            for k in key_arr:
                if add(k,arr,i,j,n,m)==True:
                    return True
    return False