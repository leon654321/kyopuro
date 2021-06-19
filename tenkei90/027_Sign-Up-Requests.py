import sys
myinput=sys.stdin.readline
N=int(myinput())
ls=set([])
for i in range(1,N+1):
    x=myinput()
    if x in ls:
        continue
    else:
        ls.add(x)
        print(i)
