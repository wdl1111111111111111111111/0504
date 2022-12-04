n, m = map(int, input().split())
d = set()
for i in range(n):
    d.add(sum(map(int, input().split())))
l = sorted(list(d))
count = 1
t = 0
for i in range(1, len(l)):
    if l[i] - l[t] >= m:
        count += 1
        t = i
print(count)