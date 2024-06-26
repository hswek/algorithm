def solution(files):
    answer = []
    arr=[]
    idx=0
    for file in files:
        head=''
        number=''
        tail=''
        number_start=True
        for i in range(len(file)):
            if file[i].isdigit()==False and i!=0 and file[i-1].isdigit()==True:
                number_start=False
                tail+=file[i]
            elif number_start==False:
                tail+=file[i]
            elif file[i].isdigit()==False and number_start==True:
                head+=file[i]
            elif file[i].isdigit()==True and number_start==True:
                number+=file[i]
        s=[head,number,tail,idx]
        arr.append(s)
        idx+=1
    arr.sort(key=lambda x:[x[0].upper(),int(x[1]),x[3]])
    for s in arr:
        answer.append(s[0]+s[1]+s[2])
                
    return answer