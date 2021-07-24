S=input()

#少しでも速度を早くしたかったので.appendの呼び出しがなくなるようにした
c=[]
cappend=c.append
h=[]
happend=h.append
o=[]
oappend=o.append
k=[]
kappend=k.append
u=[]
uappend=u.append
d=[]
dappend=d.append
a=[]
aappend=a.append
i=[]
iappend=i.append


for x in reversed(S):
    if x=="i":
        iappend(1)
    elif x=="a":
        aappend(sum(i)%(10**9+7))
    elif x=="d":
        dappend(sum(a)%(10**9+7))
    elif x=="u":
        uappend(sum(d)%(10**9+7))
    elif x=="k":
        kappend(sum(u)%(10**9+7))
    elif x=="o":
        oappend(sum(k)%(10**9+7))
    elif x=="h":
        happend(sum(o)%(10**9+7))
    elif x=="c":
        cappend(sum(h)%(10**9+7))

print(sum(c)%(10**9+7))
