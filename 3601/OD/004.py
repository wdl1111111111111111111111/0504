n,e=map(int,input().split(' '))
sum=0
x=0
y=0
for i in range(n):
    a,b=map(int,input().split(' '))
    sum+=(a-x)*abs(y)
    x=a
    y=abs(y+b)
sum=sum+(e-a)*y
print(sum)