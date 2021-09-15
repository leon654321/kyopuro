a=["ABC" , "ARC" , "AGC" , "AHC"]
 
s1=input()
s2=input()
s3=input()
 
s=[s1,s2,s3]
 
for i in a:
  if i in s:
    continue
  else:
    print(i)
    break
