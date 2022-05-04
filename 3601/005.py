dictT={'z':'A','Z':'a','9':'0'}        #加密用      
dictrT={'A':'z','a':'Z','0':'9'}        #解密用
s = input()       
s_r = ''                #用于存储加密输出
r=''                        #用于存储解密输出
rs = input()
for i in s:                        #加密过程，不解释。。应套逻辑
    if i in dictT.keys():            #先从那几个特殊的下手排查 z Z 9
        s_r+=(dictT[i])
    elif i.isdigit():
        s_r+=str((int(i)+1))
    elif i.islower():
        s_r+=(chr(ord(i.upper())+1))
    elif i.isupper():
        s_r+=(chr(ord(i.lower())+1))
    else:
        s_r+=(i)
for j in rs:                        #解密过程，依然硬套逻辑 从特殊的开始反转
    if j in dictrT.keys():
        r+=(dictrT[j])
    elif j.isdigit():
        r+=str((int(j)-1))
    elif j.islower():
        r+=(chr(ord(j.upper())-1))
    elif j.isupper():
        r+=(chr(ord(j.lower())-1))
    else:
        r+=(j)
print(s_r)
print(r)