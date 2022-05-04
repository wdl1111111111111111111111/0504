n=int(input())
m=n**0.5
print(m)
for i in range(2,int(m+1)):
    # if n %i==0:
    #     print(n)
    while n %i==0:
        print(n)
        n=n//i


