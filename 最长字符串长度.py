a=input()
if a.isdigit():
    print(-1)
elif a.isalpha():
    print(-1)
else:
    a = list(a)
    result = []
    for i in range(len(a)):
        if str(a[i]).isalpha():
            result.append(i)
    goal = []
    start = 0
    for i in range(len(result)):
        goal.append(int(result[i]) - start)
        start = int(result[i])
    if goal[0] != 0:
        goal[0] = int(goal[0]) + 1
    goal.append(len(a) - int(result[-1]))
    print(max(goal))