
# while True:
#     try:
#         n = int(input())
#         m = list(map(int,input().split()))
#         x = list(map(int,input().split()))
#     except:
#         break
#     else:
n=3
m=[1,2,3]
x=[1,2,3]
amount = []
weights = {0,}
for i in range(n):
    for j in range(x[i]):
        amount.append(m[i])
print(amount)
            
for i in amount:
    for j in list(weights):
        weights.add(i+j)
        print(weights)
    #print(weights)
print(len(weights))