a=int(input())
str_list=[]
for i in range(a):
    str=input()
    str_list.append(str)
def sum(x):
    x=x.replace('.',':')  
    h=int(x.split(":")[0])*3600*1000
    m=int(x.split(":")[1])*60*1000
    s=int(x.split(":")[2])*1000
    k=int(x.split(":")[3])
    return h+m+s+k
str_list.sort(key=lambda x:sum(x))
for str in str_list:
    print(str)