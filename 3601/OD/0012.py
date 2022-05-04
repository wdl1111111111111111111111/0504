n = int(input())
len = int(input())
ints = list(map(int , input().split()))

time = 0
more = 0

for i in ints:
    if i + more > n:
        more = i + more - n
    else:
        more = 0
    time += 1

while more > 0:
    more -= n
    time += 1

print(time)
