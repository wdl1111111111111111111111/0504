s = input()
d = {'mul': '*', 'add': '+', 'sub': '-', 'div': '/'}
s1 = ''
s2 = []
Flag=0
for i in range(len(s)):
    if s[i].isalpha():
        s1 += s[i]
    elif s[i].isdigit():
        s1 += s[i]
    elif s[i] == ' ':
        s2.append(s1)
        s1 = ''
    elif s[i] == ')': #如果检测为），就把前三个字符取出来做运算
        if s1!='':
            s2.append(s1)
            s1 = ''
        a = s2.pop()
        b = s2.pop()
        c = s2.pop()
        if c=='div' and int(a)==0: #如果除以0 输出error
            Flag="error"
            break
        r = eval(b + d[c] + a)
        s2.append(str(int(r))) #把新的结果向下取整加进数组

if Flag=="error":
    print(Flag)
else:
    print(int(s2[0]))