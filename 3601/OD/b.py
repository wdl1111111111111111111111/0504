x,y=map(int,input().split())
k=int(input())
a=[]
for i in range(k):
    a.append(list(map(int,input().split())))
print(a)
b = [[0]*y for j in range(x)]
for i in a:
    b[i[0]][i[1]]=-1
print(b)