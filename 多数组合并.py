"""
现在有多组整数数组
需要将他们合并成一个新的数组
合并规则从每个数组里按顺序取出固定长度的内容
合并到新的数组
取完的内容会删除掉
如果改行不足固定长度，或者已经为空
则直接取出剩余部分的内容放到新的数组中继续下一行

输入描述
  第一 行每次读取的固定长度
  长度0<len<10
  第二行是整数数组的数目
  数目 0<num<10000
  第3~n行是需要合并的数组
  不同的数组用换行分割
  元素之间用逗号分割
  最大不超过100个元素

 输出描述
  输出一个新的数组，用逗号分割
输入：
  示例1
  输入
      3
      2
      2,5,6,7,9,5,7
      1,7,4,3,4
  输出
      2,5,6,1,7,4,7,9,5,3,4,7
"""
N=int(input())
num=int(input())
a_list=[]
for i in range(num):
    a=input().split(',')
    a_list.append(a)
b=''
c=max([len(s) for s in a_list])
result=[]
count=0
for j in range(0,c,N):
    for i in range(len(a_list)):
        result+=a_list[i][j:j+N]
print(','.join(result))