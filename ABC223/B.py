S=input()

L=len(S)

ans=[]

#パターンが少ないので全列挙できる
#その後ソートで最初と最後取り出し
for i in range(L):
    ans.append(S[i:]+S[:i])
    
ans.sort()

print(ans[0])
print(ans[-1])
