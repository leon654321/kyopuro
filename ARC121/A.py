N=int(input())
X=[0]*N
Y=[0]*N
for i in range(N):
    x,y=map(int,input().split())
    X[i]=x
    Y[i]=y
X_a=sorted(X)
Y_a=sorted(Y)
no1_X=X_a[-1]-X_a[0]
no2_X=max(X_a[-1]-X_a[1],X_a[-2]-X_a[0])
no1_Y=Y_a[-1]-Y_a[0]
no2_Y=max(Y_a[-1]-Y_a[1],Y_a[-2]-Y_a[0])
XY=sorted([no1_X,no2_X,no1_Y,no2_Y])

Xmax=X_a[-1]
Xmin=X_a[0]
Ymax=Y_a[-1]
Ymin=Y_a[0]
cnt1=0
cnt2=0
cnt3=0
cnt4=0


for i,name in enumerate(X):
    if name==Xmax and Y[i]==Ymax:
        cnt1=1
    elif name==Xmax and Y[i]==Ymin:
        cnt2=1
    if name==Xmin and Y[i]==Ymax:
        cnt3=1
    elif name==Xmin and Y[i]==Ymin:
        cnt4=1

cnt5=cnt1+cnt4
cnt6=cnt2+cnt3
        
if (no2_Y<no1_X or no2_X<no1_Y) and (cnt5==2 or cnt6==2):
    print(XY[-3])

else:
    print(XY[-2])
