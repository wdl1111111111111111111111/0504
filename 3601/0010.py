a=input()
c=input()
abc="abcdefghijklmnopqrstuvwxyz"
s=""
for i in abc:
    if i not in a:
        s+=i
ditc={}
for i in range(len(a)):
    ditc[abc[i]]=a[i]
for i in range(len(a),26):
    ditc[abc[i]]=s[i-len(a)]
word=''
for i in c:
    word+=ditc[i]
print(word)