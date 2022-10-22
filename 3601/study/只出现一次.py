s=input()
c=[]
for i in s:
    if s.count(i)>1:
        pass
    elif s.count(i)==1:
        print(i)
        c.append(i)
        break
if len(c)==0:
    print(-1)