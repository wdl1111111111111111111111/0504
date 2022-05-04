n=int(input())
height=list(map(int,input().split()))
weight=list(map(int,input().split()))
dict={}
for i in range(n):
    dict[i+1]=(height[i],weight[i])
dict_1=sorted(dict.items(),key=lambda x:(x[1][0],x[1][1]))
for i in dict_1:
    print(i[0],end=' ')
