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