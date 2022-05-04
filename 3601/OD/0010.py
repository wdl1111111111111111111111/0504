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