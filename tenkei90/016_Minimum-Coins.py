import sys
myinput=input#sys.stdin.readline

N=int(myinput())
ls=list(map(int,myinput().split()))
ls=sorted(ls,reverse=True)

a,b,c=ls[0],ls[1],ls[2]
num=9999
N1=N//a

for i in range(N1+1):
    N2=(N-a*i)//b
    for j in reversed(range(min(10000-i,N2+1))):
        N3=(N-a*i-b*j)//c
        if a*i+b*j+c*N3==N and num>(i+j+N3):
            num=i+j+N3
            break
        elif i+j+N3>num :
            break


print(num)            
