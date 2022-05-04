n=100
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    if a==1:
        return True
    else:
        return False
for i in range(1,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if i*i+j*j==k*k and gcd(i,j) and gcd(j,k) and gcd(k,i):
                print(i,j,k)

