import sys
a,b=sys.stdin.readline().rstrip().split()
b=int(b)
result=0
for i in range(len(a)):
    try:
        e=int(a[-1-i])
        
        result+=(b**i)*e
        #print(b,i,e)
    except:
        #print((ord(a[i])-ord('A')+10))
        result+=b**i*(ord(a[-1-i])-ord('A')+10)
print(result)
