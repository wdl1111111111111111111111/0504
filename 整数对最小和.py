'''
//        给定两个整数数组
        //array1 array2  数组元素按升序排列
        // 假设从arr1 arr2中分别取出一个元素，可构成一对元素
        // 现在需要取出k对元素，并对取出的所有元素求和
        // 计算和的最小值
        // 注意：两对元素对应arr1 arr2的下标是相同的
        //       视为同一对元素

        //输入描述
        //    输入两行数组arr1 arr2
        //    每行首个数字为数组大小size   0<size<=100
        //    arr1，2中的每个元素   0< <1000
        //    接下来一行  正整数k   0<k<=arr1.size * arr2.size
        // 输出描述
        //   满足要求的最小值

        // 例子

        //输入
        //   3 1 1 2
        //   3 1 2 3
        //   2

        //输出
        //   4

'''
array_1=input().split(' ')
array_2=input().split(' ')
n=int(input())
array_3=[]
len_array_1=len(array_1)
len_array_2=len(array_2)
for i in range(len_array_1):
    for j in range(len_array_2):
        array_3.append(int(array_1[i])+int(array_2[j]))
array_3.sort()
sum=0
for i in range(n):
    sum+=array_3[i]
print(sum)