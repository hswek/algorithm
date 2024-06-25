import sys
a,b,v=map(int,sys.stdin.readline().rstrip().split())
if v<=a:
    print(1)
else:
    result=1+(v-a)//(a-b)
    if (v-a)%(a-b)!=0:
        result+=1
    print(result)