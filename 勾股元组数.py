'''
//        如果三个正整数A B C ,A²+B²=C²则为勾股数
        // 如果ABC之间两两互质，即A与B A与C B与C均互质没有公约数，
        // 则称其为勾股数元组。
//        请求出给定n m 范围内所有的勾股数元组
//        输入描述
//          起始范围 1<n<10000    n<m<10000
//        输出目描述
//           abc 保证a<b<c输出格式  a b c
//           多组勾股数元组 按照a升序b升序 c升序的排序方式输出。
//           给定范围内，找不到勾股数元组时，输出  Na

        // 案例
        //  输入
        //   1
        //   20
        //  输出
        //   3 4 5
        //   5 12 13
        //   8 15 17

        //  输入
        //    5
        //    10
        //  输出
        //    Na
'''
from itertools import count


n=int(input())
N=int(input())
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    if a==1:
        return True
    else:
        return False
count=0
for i in range(n,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if i*i+j*j==k*k and gcd(i,j) and gcd(j,k) and gcd(k,i):
                print(i,j,k)
                count+=1
if count==0:
    print("Na")
            # else:
            #     print("Na")
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    if a==1:
        return True
    else:
        return False
for i in range(1,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if i*i+j*j==k*k and gcd(i,j) and gcd(j,k) and gcd(k,i):
                print(i,j,k)