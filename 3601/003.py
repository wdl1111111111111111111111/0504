from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG


#a="A10;S20;W10;D30;X;A1A;B10A11;;A10;"
a="A10;S20;W10;D30;X;A1A;B10A11;;A10;"
a=a.split(";")
b=[]
for i in range(len(a)):
    if len(a[i])==2 or len(a[i==3]):
        if a[i].startswith('A') or a[i].startswith("D") or a[i].startswith('W') or a[i].startswith("S"):
            for s in "0123456789":
                if a[i].endswith(s):
                    b.append(a[i])
        else:
            pass
d=[]
for num in b:
    if num[0]=="A":
        d.append((-int(num[1:]),0))
    elif num[0]=="D":
         d.append((num[1:],0))
    elif num[0]=="W":
         d.append((0,num[1:]))
    elif num[0]=="S":
         d.append((0,-int(num[1:])))
print(d)
m=0
n=0
for i in range(len(d)):
    m+=int(d[i][0])
    n+=int(d[i][1])
print(m,n)

