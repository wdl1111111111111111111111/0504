
str_1=input()
array=input().split(' ')
len_array=len(array)
for i in range(len_array):
    if array[i]==str_1 and array[i+2]=="00":
        n=int(array[i+1].strip('0'))
        for s in array[i+3:i+3+n]:
            print(s,end=' ')

