N=int(input())
S=input()

a=[]
aappend=a.append
t=[]
tappend=t.append
c=[]
cappend=c.append
o=[]
oappend=o.append
d=[]
dappend=d.append
e=[]
eappend=e.append
r=[]
rappend=r.append

for x in reversed(S):
    if x=="r":
        rappend(1)
    elif x=="e":
        eappend(sum(r))
    elif x=="d":
        dappend(sum(e))
    elif x=="o":
        oappend(sum(d))
    elif x=="c":
        cappend(sum(o))
    elif x=="t":
        tappend(sum(c))
    elif x=="a":
        aappend(sum(t))

print(sum(a)%(10**9+7))
