
s=[[20,17],[20,16],[15,11],[10,10],[9,10],[9,20]]
s=sorted(s,key=lambda x:[x[0],x[1]])
result=1
dp=[1 for i in range(len(s))]
for i in range(1,len(s)):
    temp=s[i]
    for j in range(0,i):
        temp_1=s[j]
        if temp[0]>temp_1[0] and temp[1]>temp_1[1]:
            dp[i]=max(dp[i],dp[j]+1)
        result=max(result,dp[i])
print(result)
