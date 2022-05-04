a = "aaaaaaaaaaaaaaabbbbbbbbbbbccccccdddddddddeeee"
# 先分别统计每个元素出现的次数
d = {}
for i in a:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
print(d)
# 再次遍历去掉次数最少的
for j in d.keys():
    # 判断等于最小的次数  min(d.values())
    if d[j] == max(d.values()):
        a = a.replace(j, '')
print(a)
