import sys

S=input()
T=input()

if S==T:
    print("Yes")
    sys.exit()


i1=0
i2=0

cnt=0
for i in range(len(S)):
    if S[i]==T[i]:
        continue
    elif cnt==0:
        cnt=1
        i1=i
    elif cnt==1:
        cnt=2
        i2=i
    else:
        cnt+=1

if cnt!=2 or (i1+1!=i2):
    print("No")
    sys.exit()

    
if S[i1]==T[i2] and S[i2]==T[i1]:
    print("Yes")
else:
    print("No")
