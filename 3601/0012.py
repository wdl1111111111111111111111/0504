dp=[[1] *20 for _ in range(12)]
for col in range(1,7):
    for row in range(1,3):
        dp[col][row]=dp[col-1][row]+dp[col][row-1]
print(dp[6][2])