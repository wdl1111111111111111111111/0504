a,b=list(map(int,input().split(" ")))
c=list(map(int,input().split(" ")))
c=sorted(c)
num=0
temp=0
for i in range(len(c)):
    temp+=c[i]
    if temp==a:
        num+=1
  elif temp>a:
        num+=1
        temp=c[i]
print(num)
