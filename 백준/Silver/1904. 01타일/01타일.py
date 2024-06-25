n=int(input())
o=[0]*(1000001)
o[1]=1
o[2]=2
for i in range(3,1000001):
    o[i]=(o[i-1]+o[i-2])%15746
print(o[n])