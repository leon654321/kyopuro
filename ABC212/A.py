#入力
A,B=map(int,input().split())

# 各条件に従い場合分け
if A>0 and B==0:
    print("Gold")
    
elif A==0 and 0<B:
    print("Silver")
    
elif 0<A and 0<B:
    print("Alloy")
