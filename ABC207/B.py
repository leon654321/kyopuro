import sys
#入力
A,B,C,D=map(int,input().split())

#水色のボールの増加速度の方が大きいとき
if D*C-B<=0:
    print(-1)
    sys.exit()


ans=A//(D*C-B)

#例外処理
if A%(D*C-B) !=0:
    ans+=1
    
    
print(ans)
