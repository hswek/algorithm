import sys
a,b=sys.stdin.readline().rstrip().split()
tmp_a=''
for i in range(len(a)-1,-1,-1):
    tmp_a+=a[i]
tmp_b=''
for i in range(len(b)-1,-1,-1):
    tmp_b+=b[i]  
a=int(tmp_a)
b=int(tmp_b)
if a>b:
    print(a)
else:
    print(b)