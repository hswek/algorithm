import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

def get_include_middle(start,mid,end):
    height=min([arr[mid],arr[mid-1]])
    i=mid-2
    j=mid+1
    length=2
    area=height*length
    while(i>=start and j<end):
        #print(i,start,j,end)
        if arr[i]>arr[j]:
            height=min(height,arr[i])
            i-=1
            length+=1
            area=max(area,length*height)
        else:
            height=min(height,arr[j])
            j+=1
            length+=1
            area=max(area,length*height)
    while(i>=start):
        height=min(height,arr[i])
        i-=1
        length+=1
        area=max(area,length*height)
    while(j<end):
        height=min(height,arr[j])
        j+=1
        length+=1
        area=max(area,length*height)
    return area

def answer(start,end):
    if start+1==end:
        return arr[start]
    mid=(start+end)//2
    first=answer(start,mid)
    two=answer(mid,end)
    three=get_include_middle(start,mid,end)
    return max([first,two,three])


print(answer(0,len(arr)))
  