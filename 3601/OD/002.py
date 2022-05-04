a = input()
zs_list = [] #接收单个正整数
fs_list =[]  #接收负整数字符串
i = 0
while i <len(a):
    temp =a[i]
    # 取正数
    if a[i].isdigit():
        zs_list.append(a[i])
    else:
        #取负数字符串
        if a[i] == '-':
            b = a[i+1:] #截取负号后面的字符串
            str1 = ''
            for fs in b:
                if fs.isdigit():
                    str1+=fs
                else:
                    break

            if str1 != '':
                fs_list.append('-'+str1)
                i = i + len(str1)
    i = i +1


zs_list.extend(fs_list)
sum =0
for x in zs_list:
    sum = sum +eval(x)
print(sum)