a=""
b=""


N=sorted(input(),reverse=True)

for i in range(len(N)):
    if i%2==0:
        a+=N[i]
    else:
        b+=N[i]

for i in range(len(b)):
    if a[i]==b[i]:
        continue
    else:
        a,b= a[:i]+b[i]+a[i+1:] ,b[:i]+a[i]+b[i+1:]
        break
        
ans=int(a)*int(b)
print(ans)
