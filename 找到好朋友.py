"""
题目描述：

在学校中，N 个小朋友站成一队，第 i 个小朋友的身高为 height[i]，第 i 个小朋友可以看到第一个比自己身高更高的小朋友j，那么 j 是 i 的好朋友 (要求：j>i) 。
请重新生成一个列表，对应位置的输出是每个小朋友的好朋友的位置。
如果没有看到好朋友，请在该位置用0代替。
小朋友人数范围 0~40000。
输入描述：

第一行输入 N，N 表示有N个小朋友
第二行输入 N 个小朋友的身高 height[i]，都是整数
输出描述：

输出 N 个小朋友的好朋友的位置
输入：

2
100 95
输出：

0 0
"""
N=int(input())
height=[int(x) for x in input().split()]
friend=['0' for n in range(N) ]
for i in range(N):
    for j in range(i+1,N):
        if height[j]>height[i]:
            friend[i]=str(j)
            break
print(friend)
print(' '.join(friend))