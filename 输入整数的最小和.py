"""
题目描述：

输入字符串s输出s中包含所有整数的最小和
说明：

字符串s只包含az,AZ,+,-，
合法的整数包括正整数，一个或者多个0-9组成，如：0,2,3,002,102
负整数，负号开头，数字部分由一个或者多个0-9组成，如-2,-012,-23,-00023
输入描述：

包含数字的字符串
输出描述：

所有整数的最小和
示例

输入：

bb1234aa
输出：

10
输入：

bb12-34aa
输出：

-31
说明：

1+2-(34)=-31
"""
a=input('')
b=""
for s in a:
    if s.isalpha():
        s=' '
    b+=s
b=b.replace("-"," -")
b=b.split(" ")
sum=0
c=[]
for i in range(len(b)):
    if len(b[i])==0:
        continue
    else:
        c.append(b[i])
for i in range(len(c)):
    if int(c[i])<=0:
        sum+=int(c[i])
    else:
        for s in c[i]:
            sum+=int(s)
print(sum)
