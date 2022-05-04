
from posixpath import split
from re import I
from turtle import window_height


n=int(input())
height=input().split()
weigt=input().split()
#arr1=[]
dict=[]
for i in range(n):
    d=dict.append(((height[i],weigt[i]),i+1))
   # arr1.append((int(height[i]),int(weigt[i])),i+1)
d=list(d)
print(d)