n=int(input())
b=1
for i2 in range(n):
    i=i2
    result=i
    while(i!=0):
        result+=i%10
        i=i//10
    if result==n:
        b=0
        print(i2)
        break
if b==1:
    print(0)