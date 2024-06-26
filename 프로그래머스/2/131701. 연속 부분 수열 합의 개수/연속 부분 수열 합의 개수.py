
def solution(elements):
    answer = 0
    elements=elements+elements
    arr=[0]*(len(elements)+1)
    arr[0]=elements[0]
    for i in range(1,len(elements)):
        arr[i]=arr[i-1]+elements[i]
    d=[]
    for i in range(-1,len(elements)):
        for j in range(i+1,min(len(elements),i+1+len(elements)//2)):
            if i==-1:
                tmp=arr[j]
            else:
                tmp=arr[j]-arr[i]
            #print(i,j,tmp)
            d.append(tmp)
    d=set(d)
    #print(d)
    return len(d)
                
            
        
    return answer