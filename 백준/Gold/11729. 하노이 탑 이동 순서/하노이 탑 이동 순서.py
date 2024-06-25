import sys
result=0
def hanoi(n,a,b,c):
    global result
    if n==1:
        print(a,c)
        result+=1
        return
    hanoi(n-1,a,c,b)
    print(a,c)
    hanoi(n-1,b,a,c)
def hanoi2(n,a,b,c):
    global result
    if n==1:
        result+=1
        return
    hanoi2(n-1,a,c,b)
    result+=1
    hanoi2(n-1,b,a,c)

n=int(input())
hanoi2(n,1,1,1)
print(result)
hanoi(n,1,2,3)