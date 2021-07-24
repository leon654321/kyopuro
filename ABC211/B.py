import sys
S=[]

for _ in range(4):
    S.append(input())
    
s=["HR","3B","2B","H"]

for i in s:
    if i in S:
        S.remove(i)
    else:
        print("No")
        sys.exit()
print("Yes")
