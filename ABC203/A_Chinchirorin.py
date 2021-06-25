#問題文
#https://atcoder.jp/contests/abc203/tasks/abc203_a

#入力
a,b,c=map(int,input().split())

#どれか二つが同じかの比較
if a==b:
    print(c)
elif b==c:
    print(a)
elif c==a:
    print(b)
    
#どれも違う値のとき
else:
    print(0)
    
