a=input()
len_a=len(a)
k=len_a//8
m=len_a%8
if k>0:
    for i in range(k):
        print(a[8*i:8*i+8])
    if m>0:
        s=a[k*8:]+(8-int(m))*'0'
        print(s)
else:
    s = a + (8 - int(len_a)) * '0'
    print(s)
