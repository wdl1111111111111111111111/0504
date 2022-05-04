a=eval(input())
one_list=sorted(a,key=lambda x:(x[0],x[1]))
num=1
len_num=len(one_list)
print(one_list)
for i in range(len_num-1):
    if one_list[i+1][1]>=one_list[i][1]:
        num+=1
print(num)
