'''
 给出n阶方阵里所有数
        求方阵里所有数的和
        输入描述：
          输入有多个测试用例
          每个测试用例第一个第一个整数n   n<=1000 表示方阵阶数为n
          接下来是n行的数字，每行n个数字用空格隔开
        输出描述：
          输出一个整数表示n阶方阵的和
        例子：
          输入
              3
              1 2 3
              2 1 3
              3 2 1
          输出
              18
'''
n=int(input())
sum=0
for i in range(n):
    a_list=list(map(int,input().split(' ')))
    for i in range(len(a_list)):
        sum+=a_list[i]
print(sum)