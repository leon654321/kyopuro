import sys
myinput=input#sys.stdin.readline
import math
mdeg=math.degrees
msin=math.sin
mcos=math.cos
matan=math.atan
msq=math.sqrt
mpi=math.pi

T=int(myinput())
L,X,Y=map(int,myinput().split())
q=t=int(myinput())

for _ in range(q):
    e=int(myinput())
    #x=X
    y=-(L/2)*msin(e/T*2*mpi)-Y
    z=(L/2)*(1-mcos(e/T*2*mpi))
    if X==0 and y==0:
        print(0.00000000)
        continue
    ans=mdeg(matan(z/msq(X**2+y**2)))
    print(ans)
