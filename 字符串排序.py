'''
 给定两个字符串
        从字符串2中找出字符串1中的所有字符
        去重并按照ASCII码值从小到大排列
        输入字符串1长度不超过1024
        字符串2长度不超过100

        字符范围满足ASCII编码要求，按照ASCII由小到大排序

        输入描述：
         bach
         bbaaccddfg
         输出
          abc

          2
          输入
          fach
          bbaaccedfg
          输出
          acf
'''
a=list(set(input()))
b=input()
a_list=[]
for s in a:
    if b.count(s)>=1:
        a_list.append(s)
print(''.join(sorted(a_list)))