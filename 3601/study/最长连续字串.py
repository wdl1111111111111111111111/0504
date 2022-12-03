s=list(map(int,input().split(" ")))
N=int(input())
max_len=-1
sum=0
for i in range(len(s)-1):
    sum+=s[i]
    for j in  range(i+1,len(s)):
        sum+=s[j]
        if sum>N:
            break
        elif sum==N:
            max_len=max(max_len,j-i+1)
            break
print(max_len)

