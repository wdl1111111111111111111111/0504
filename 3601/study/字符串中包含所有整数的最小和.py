s=input()
new_s=''
list=[]
count=0
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        i=' '
    elif i=='-':
        i=' '+'-'
    new_s+=i
new_s=new_s.split(" ")
for i in range(len(new_s)):
    if new_s[i]=='':
        continue
    else:
        list.append(new_s[i])
def sum(s):
    if int(s)<0:
        return int(s)
    else:
        sum=0
        for i in s:
            sum+=int(i)
        return sum
for j in list:
    count=sum(j)+count
print(count)

