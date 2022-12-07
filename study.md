

## 找终点

```
nums = list(map(int, input().split()))
length = len(nums)
res = []
for i in range(1, length // 2):
    step = 1
    index = i
    while index < length - 1:
        index += nums[index]
        step += 1
    if index == length - 1:
        res.append(step)
if len(res) > 0:
    res.sort()
    print(res[0])
else:
    print(-1)
```

##  出错的或电路

![在这里插入图片描述](https://img-blog.csdnimg.cn/25e586dfc0c94d36a9db984698140f25.png)

```
 
s1 = "110"
s2 = "110"
n=3
s1_zero = s1.count("0")
s1_one = s1.count("1")
s2_zero = 0
s2_one = 0
for i in range(n):
    if s2[i]=="0" and s1[i] == "0":
        s2_zero +=1
    if s2[i] == "0" and s1[i] == "1":
        s2_one += 1
 
total = s1_zero*s2_one + s1_one*s2_zero
print(total)
print(s1_zero)
```

## 路灯照明问题

```
一条笔直的公路上安装了N个路灯，从位置0开始安装，路灯之间的距离是100m。每个路灯都有自己的照明半径，请计算第一个路灯和最后一个路灯之间，未照明区间的长度和。
输入描述：
第一行为一个数N，表示灯的个数，[1, 100000] 第二行为N个空格分隔的数，表示路灯的照明半径，[1,100*100000]
输出描述：
第一个路灯和最后一个路灯之间，未照明区间的长度和
举例：
输入：2 50 50 输出：0
输入：4 50 70 20 70 输出：20
输入：8 10 10 10 250 10 10 10 10 输出：160
```

```
if __name__ == "__main__":
    N = 8
    Lights = list(map(int, "10 10 10 250 10 10 10 10".split()))
    res = []
    LightSum = 0
    for i in range(N):
        left = max(0, 100*i-Lights[i])
        right = min((N-1)*100, 100*i+Lights[i])
        while len(res) > 0 and res[-1][1] > left:
            left_new, right_rew = res.pop(len(res)-1)
            LightSum -= right_rew - left_new
            left = min(left_new, left)
            right = max(right_rew, right)
        LightSum += right - left
        res.append([left, right])
    print((N-1)*100 - LightSum)
```

## 最长数字串

```
import re
s= input().strip()
pattern = "[+-]?\d+(\\.\d+)?"
res = ""
for i in range(len(s)):
    temp = s[i:]
    result = re.search(pattern,temp)
    if result:
        if len(result.group(0)) >= len(res):
            res = result.group(0)
print(res)
```

## 查找接口成功率最优时间段

```
min_aver = int(input().strip())
nums = map(int,input().strip().split(" "))
 
temp = []
res = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        if sum(nums[i:j]) <= min_aver*(j-i+1):
            res.append([len(nums[i:j]),i,j-1])
            
new_res = sorted(res,key=lambda x:x[0],reverse=True)
max_num = new_res[0][0]
result = []
for i in new_res:
    if i[0] == max_num:
        print("-".join([str(i[1]),str(i[-1])]))
    else:
        break
```

## 最长的密码

```
import sys
def solution_01():
    # 处理输入
    pwd_list = input().split(" ")
 
    valid_pwd_list = []  # 定义变量,存储合法的密码
    for pwd in pwd_list:
        flag = True  # 定义flag, 表示当前密码依次去掉一个字符后是否都在pwd_list中
        # 当前密码依次去除一个字符
        for i in range(len(pwd) - 1, 0, -1):
            if pwd[: i] not in pwd_list:
                flag = False
                break
        if flag:
            valid_pwd_list.append(pwd)
 
    valid_pwd_list.sort(reverse=True)
 
    return valid_pwd_list[0] if len(valid_pwd_list) != 0 else ""
 
 
if __name__ == '__main__':
    ans = solution_01()
    print(ans)
```

## 计算数组中心位置

```
import sys
# 计算num_list的乘积
def calc_pd(num_list):
    pd = 1
    for num in num_list:
        pd *= num
 
    return pd
 
 
def Solution():
    # 处理输入
    num_list = input().split(" ")
    num_list = [int(num) for num in num_list]
 
    ans = -1
    for i in range(0, len(num_list)):
        if i == 0:
            l_pd = 1
            r_pd = calc_pd(num_list[1:])
        elif i == len(num_list) - 1:
            l_pd = calc_pd(num_list[0: -1])
            r_pd = 1
        else:
            l_pd = calc_pd(num_list[0: i])
            r_pd = calc_pd(num_list[i + 1:])
        if l_pd == r_pd and ans == -1:
            ans = i
 
    return ans
 
 
if __name__ == '__main__':
    ans = Solution()
    print(ans)
```

## 积木最远距离

```
count = int(input())
blocks = {}
for i in range(count):
    num = int(input())
    if num in blocks:
        blocks[num].append(i)
    else:
        blocks[num] = [i]
 
max_distance = -1
for block_num in blocks:
    if len(blocks[block_num]) > 1:
        max_distance = max(max_distance, max(blocks[block_num]) - min(blocks[block_num]));
 
print(max_distance)
```

## 垃圾短信识别

```
import collections
 
 
def solution_01():
    # 处理输入
    total_num = int(input())
    relation_map = {}  # 构建关系映射
    for i in range(total_num):
        id_list = input().split(" ")
        if id_list[0] not in relation_map.keys():
            relation_map[id_list[0]] = [id_list[1]]
        else:
            relation_map[id_list[0]].append(id_list[1])
 
    spec_id = input()
 
    # 计算L, 即A发送过短信的接收者中,没有给A发送过短信的人; L>5
    send_id_list = relation_map[spec_id] if spec_id in relation_map.keys() else []
    num_send_2_A = 0  # 定义变量,A发送给短信的接收者中,给A发过短信的人数
    for id_ in send_id_list:
        if id_ in relation_map.keys():
            if spec_id in relation_map[id_]:
                num_send_2_A += 1
 
    L = len(send_id_list) - num_send_2_A
 
    # 计算M, 即A发送的短信数-A接收的短信数; M>10
    num_A_received = 0  # 定义变量,A接收到的短信数
    for k, v in relation_map.items():
        if k != spec_id and spec_id in v:
            num_A_received += 1
 
    M = len(send_id_list) - num_A_received
 
    # 计算N, 即如果存在X,A发送给X的短信数-A接收到X的短信数; N>5
    N = -1
    if spec_id in relation_map.keys():  # 存在A发送过短信的情况
        spec_count = collections.Counter(relation_map[spec_id])  # 统计A发送给其他ID各自的短信数
        for k, v in spec_count.items():
            if k in relation_map.keys():  # 如果X发送过短信
                k_count = collections.Counter(relation_map[k])  # 统计X发送给其他ID各自的短信数
                if spec_id in k_count.keys():  # X给A发过短信
                    d_value = int(v) - int(k_count[spec_id])  # 计算差值
                    N = max(N, d_value)
 
    if L > 5 or M > 10 or N > 5:
        print(f"true {L} {M}")
    else:
        print(f"false {L} {M}")
 
 
if __name__ == '__main__':
    solution_01()
```

## 打印机队列

```
import functools
from collections import defaultdict
targs_dict = defaultdict(list)
total = int(input().strip())
count = 0
def comp(x,y):
    if x[0] ==y[0]:
        if x[1] < y[1]:
            return -1
        else:
            return 1
    if x[0] < y[0]:
        return 1
    else:
        return -1
for i in range(total):
    temp_msg = input().strip().split(" ")
    # temp_msg = msg_list[i]
    if temp_msg[0] =="IN":
        count+=1
        temp_key = int(temp_msg[1])
        temp_value = (int(temp_msg[2]),count)
        targs_dict[temp_key].append(temp_value)
    else:
        # print(targs_dict)
        temp_key = int(temp_msg[1])
        temp_targs = targs_dict[temp_key]
        if temp_targs == []:
            print("NULL")
        else:
            temp_targs.sort(key=functools.cmp_to_key(comp))
            print(temp_targs[0][1])
            # print(temp_targs)
            targs_dict[temp_key] = temp_targs[1:]
```

## 模拟商场优惠打折

```
#先满减后打折
def mode_a(price,m,n):
    count = 0
    while m>0:
        if price < 100:
            break
        price -= (price // 100 * 10)
        count += 1
        m-=1
    price *= 0.92
    count +=1
    return (price, count)
 
#先打折后满减
def mode_b(price, m, n):
 
    count = 0;
    price *= 0.92
    count +=1
    while m>0 :
        if price < 100:
            break
        price -= (price // 100 * 10)
        count += 1
        m -= 1
    return (price, count)
 
 
#先满减后无门槛
def mode_c(price, m, k):
 
    count = 0
    while m>0 :
        if price < 100:
            break
        price -= (price // 100 * 10)
        count += 1
        m -= 1
 
    for i in range(k):
        price -= 5
        count +=1
        if price < 0:
            break
    return (price, count)
 
# 先打折后无门槛
def mode_d(price, n, k):
 
    count = 0
    price *= 0.92
    count += 1;
    for i in range(k):
        price -= 5
        count +=1
        if price < 0:
            break
    return (price, count)
 
def main():
 
    #处理输入
    # params = list(map(int,input().strip().split("")))
    #
    # m = params[0]
    # n = params[1]
    # k = params[2]
    params = [3,2,5]
    m,n,k = 3,2,5
    # nums = int(input().strip())
    nums= 3
    prices=[100,200,400]
    for i in range(nums):
        res = []
        # price = int(input().strip())
        price = prices[i]
        res.append(mode_a(price, m, n))
        res.append(mode_b(price, m, n))
        res.append(mode_c(price, m, k))
        res.append(mode_d(price, n, k))
 
        #按照价格降序，用券数降序排序
        res.sort(key=lambda x: (x[0], x[1]))
        print(res[0])
main()
```

# 最大化控制资源成本

```
# coding:utf-8
import functools
 
max_machine = 0
 
# 处理输入
task_num = input()
 
i = int(task_num)
ranges = []
while i > 0:
    input_str = input()
    input_list = [int(x) for x in input_str.split(" ")]
    ranges.append(input_list)
    i = i - 1
 
 
# 自定义排序函数，a,b为两个list
def comp(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] == b[0]:
        if a[1] > b[1]:
            return 1
        elif a[1] == b[1]:
            return 0
    return -1
 
 
# 求公共区间
def cal_public_range(ranges):
    global max_machine
    ranges = sorted(ranges, key=functools.cmp_to_key(comp))
    public_range = []
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            left = max(ranges[i][0], ranges[j][0])
            right = min(ranges[i][1], ranges[j][1])
            if left <= right:
                temp = [left, right, ranges[i][2] + ranges[j][2]]
                public_range.append(temp)
                if ranges[i][2] + ranges[j][2] > max_machine:
                    max_machine = ranges[i][2] + ranges[j][2]
    return public_range
 
 
while len(ranges) > 1:
    ranges = cal_public_range(ranges)
 
print(max_machine)
```

## 羊农夫狼过河

```
input_nums = [int(x) for x in input().split(" ")]
M = input_nums[0]
N = input_nums[1]
X = input_nums[2]
 
min_times = (M + N) * X
 
 
# m0, n0 分别表示剩余的羊、狼个数， x为船容量
# m1, n1 分别表示运输到对岸的羊、狼个数，times为次数
def transport(m0, n0, x, m1, n1, times):
    global min_times
    # 若可以一次性运走，结束了，注意等于号。。。
    if x >= m0 + n0:
        if times + 1 < min_times:
            min_times = times + 1
        return times + 1
 
    # 尝试运一部分狼一部分羊
    # 要上船的羊数量不可以超过岸上数量、也不可以超过船的容量
    for i in range(m0):
        if i > x:
            break
        # 要上船的狼的数量不可以超过岸上数量、也不可以超过船装了羊后的剩余的容量
        for j in range(n0):
            if i + j > x:
                break
            # 不可以不运
            if i + j == 0:
                continue
 
            # 船离岸后，原来这岸，要么没有羊，要么羊比狼多，才可以运；对岸也要检查，不考虑回程带动物
            if (m0 - i == 0 or m0 - i > n0 - j) and (m1 + i == 0 or m1 + i > n1 + j):
                # 运一次
                result = transport(m0 - i, n0 - j, x, m1 + i, n1 + j, times + 1)
                # 如果获取了结果，和minTime比较，但是不结束，继续检查
                if result < min_times and result != 0:
                    min_times = result
 
    # 没有方案...返回0
    return 0
 
 
# 表示已运输到对岸的羊、狼个数
m_temp = 0
n_temp = 0
 
transport(M, N, X, m_temp, n_temp, 0)
 
if min_times == (M + N) * X:
    print(0)
else:
    print(min_times)
```

## 真正的密码

```
# 处理输入
input_strs = input().split(" ")
# 将所有字符串放入哈希集合
word_set = set()
for single_str in input_strs:
    word_set.add(single_str)
# 真正的密码
true_pass_word = ""
 
# 按顺序检查每一个词
for single_str in input_strs:
    # 条件1：检查这个词所有以索引0开头的子串在数组中是否都有
    flag = True
    for i in range(1, len(single_str)):
        # 以索引0开头的子串
        sub_str = single_str[0:i]
        if sub_str not in word_set:
            flag = False
            break
 
    if flag:
        # 条件2：比较密码长度
        if len(single_str) > len(true_pass_word):
            true_pass_word = single_str
        # 条件3：比较密码字典排序
        if len(single_str) == len(true_pass_word) and single_str > true_pass_word:
            true_pass_word = single_str
 
print(true_pass_word)
```

## 过滤组合字符串

```
import copy
 
# 保存排列组合字符串
res_str_list = []
 
# 预设值
num_char_map = {'0': "abc", '1': "def", '2': "ghi", '3': "jkl", '4': "mno", '5': "pqr", '6': "st", '7': "uv", '8': "wx",
                '9': "yz"}
 
 
# 递归求排列组合
def dfs(num_str, temp_list, index):
    if index == len(num_str):
        res_str_list.append("".join(temp_list))
        return
    temp_list_back_up = copy.copy(temp_list)
    for single_char in num_char_map[num_str[index]]:
        temp_list.append(single_char)
        dfs(num_str, temp_list, index + 1)
        temp_list.pop()
 
 
# 处理输入
num_str = input()
block_str = input()
dfs(num_str, [], 0)
 
# 过滤
for single_str in res_str_list:
    if block_str in single_str:
        res_str_list.remove(single_str)
 
print(res_str_list)
```

## 等和子数组最小和

```
import functools
 
 
def canPartitionKSubsets(nums, k):
    all = sum(nums)
    if all % k:
        return False
    per = all // k
    nums.sort()
    if nums[-1] > per:
        return False
    n = len(nums)
    dp = [False] * (1 << n)
    dp[0] = True
    cursum = [0] * (1 << n)
    for i in range(0, 1 << n):
        if not dp[i]:
            continue
        for j in range(n):
            if cursum[i] + nums[j] > per:
                break
            if (i >> j & 1) == 0:
                next = i | (1 << j)
                if not dp[next]:
                    cursum[next] = (cursum[i] + nums[j]) % per
                    dp[next] = True
    return dp[(1 << n) - 1]
 
 
# 处理输入
n = int(input())
nums = [int(x) for x in input().split(" ")]
 
for i in reversed(range(n + 1)):
    # 从最大的可能行开始，满足条件即为为最小的情况
    if (canPartitionKSubsets(nums, i)):
        print(sum(nums) / i)
        break;
```

## 最多颜色的车辆

```
cars = [int(x) for x in input().split(" ")]
window_size = int(input())
 
car_count = [0, 0, 0]
# 初始化滑动窗口
for i in range(window_size):
    car_count[cars[i]] += 1
 
# 滑动窗口向前滑
max_res = max(max(car_count[0], car_count[1]), car_count[2])
for i in range(window_size, len(cars)):
    car_count[cars[i]] += 1
    car_count[cars[i - window_size]] -= 1
    max_res = max(max_res, max(max(car_count[0], car_count[1]), car_count[2]))
print(max_res)
```

## 完美走位

```
# 处理输入
input_str = input()
 
char_count = {'W': 0, 'A': 0, 'S': 0, 'D': 0}
 
# 频次统计
for single_char in input_str:
    char_count[single_char] += 1
 
# 特殊情况
if char_count['W'] == char_count['A'] and \
        char_count['W'] == char_count['S'] and \
        char_count['W'] == char_count['D']:
    print(0)
else:
    # 左右区间位置
    left = 0
    right = 0
    length = 0
 
    # 替换的最小长度
    res = len(input_str)
    # 出现次数最多的字母
    max_char_num = 0
    # 可替换字母个数, 随着指针移动，如果free_char_num 大于0且能被4整除，当前范围满足条件，左指针右移一格，否则右指针右移
    free_char_num = 0
 
    char_count[input_str[0]] -= 1
    while True:
        max_char_num = max(max((max(char_count['W'], char_count['S'])), char_count['A']), char_count['D']);
        length = right - left + 1
        free_char_num = length - ((max_char_num - char_count['W']) + (max_char_num - char_count['S']) + (
                max_char_num - char_count['A']) + (max_char_num - char_count['D']));
        if free_char_num >= 0 and free_char_num % 4 == 0:
            if length < res:
                res = length
 
            char_count[input_str[left]] += 1
            left += 1
 
        else:
            right += 1
            char_count[input_str[right]] -= 1
 
        if right >= len(input_str) - 1:  # 越界即结束
            break
 
    print(res)
```

## 字符串重新排列

```
# 处理输入
input_str = input()
 
char_count = {'W': 0, 'A': 0, 'S': 0, 'D': 0}
 
# 频次统计
for single_char in input_str:
    char_count[single_char] += 1
 
# 特殊情况
if char_count['W'] == char_count['A'] and \
        char_count['W'] == char_count['S'] and \
        char_count['W'] == char_count['D']:
    print(0)
else:
    # 左右区间位置
    left = 0
    right = 0
    length = 0
 
    # 替换的最小长度
    res = len(input_str)
    # 出现次数最多的字母
    max_char_num = 0
    # 可替换字母个数, 随着指针移动，如果free_char_num 大于0且能被4整除，当前范围满足条件，左指针右移一格，否则右指针右移
    free_char_num = 0
 
    char_count[input_str[0]] -= 1
    while True:
        max_char_num = max(max((max(char_count['W'], char_count['S'])), char_count['A']), char_count['D']);
        length = right - left + 1
        free_char_num = length - ((max_char_num - char_count['W']) + (max_char_num - char_count['S']) + (
                max_char_num - char_count['A']) + (max_char_num - char_count['D']));
        if free_char_num >= 0 and free_char_num % 4 == 0:
            if length < res:
                res = length
 
            char_count[input_str[left]] += 1
            left += 1
 
        else:
            right += 1
            char_count[input_str[right]] -= 1
 
        if right >= len(input_str) - 1:  # 越界即结束
            break
 
    print(res)
```

## 字符串子序列

```
a = input().strip()
b = input().strip()
 
j = len(b) - 1
ok = True
for i in range(len(a) - 1, -1, -1):
    if j == -1:
        print(-1)
        exit(0)
    find = False
    for k in range(j, -1, -1):
        if a[i] == b[k]:
            j = k - 1
            find = True
            break
    if not find:
        ok = False
if not ok:
    print(-1)
else:
    print(j + 1)
```

## 事件推送

```
m, n, r = map(int, input().split())
numsA = list(map(int, input().split()))
numsB = list(map(int, input().split()))
for ai in numsA:
    for bj in numsB:
        if ai <= bj and bj - ai <= r:
            print(ai, bj)
            break
```

## 最大股票收益

```
def to_rmb(n):
    if n[-1] == "Y":
        return int(n[:-1])
    else:
        return int(n[:-1]) * 7
 
 
while 1:
    try:
        nums = list(map(to_rmb, input().split()))
 
        if not nums:
            print(0)
            break
 
        dp = []
        # 最大收益
        max_ = 0
        # 当前最小值
        min_ = nums[0]
        before_ = nums[0]
        for c in nums:
            if before_ > c:
                dp.append(max_)
                min_ = c
                max_ = 0
            else:
                min_ = min(min_, c)
                max_ = max(max_, c - min_)
            before_ = c
 
        dp.append(max_)
        print(sum(dp))
    except Exception as e:
        break
```

## 射击比赛成绩

```
while 1:
    try:
        n = int(input())
        ids = input().split(",")
        nums = list(map(int, input().split(",")))
 
        # 记录用户成绩
        dct = {}
        for i in range(n):
            if ids[i] in dct:
                dct[ids[i]].append(nums[i])
            else:
                dct[ids[i]] = [nums[i]]
 
        # 剔除长度小于3的用户
        for k, v in dct.items():
            if len(v) < 3:
                dct.pop(k)
            else:
                v.sort(reverse=True)
                dct[k] = sum(v[:3])
 
        ret = sorted(dct.items(), key=lambda x: (x[1], x[0]), reverse=True)
        print(",".join([id_ for id_, v in ret]))
    except Exception as e:
        break
```

## 最长广播效应

```
n = 5
t = 7
link_list = [[2,1],[1,4],[2,4],[2,3],[3,4],[3,5],[4,5]]
def bfs():
    queue = [2] #添加起点值
    queue1 = []
    visited = [2]#讲起点值放入已访问列表，防止重复计算
    a= 0
    while queue:
        m = queue.pop(0)
        for k,v in  enumerate(link_list):
            non_m = v[0] if m!=v[0] else v[1]
            if m in v and non_m not in visited:
                visited.append(non_m)
                queue1.append(non_m)
                link_list.pop(k)
        if len(queue1)>0:
            a+=1
            queue = queue1
            queue1 = []
    return a*2
print(bfs())
```

