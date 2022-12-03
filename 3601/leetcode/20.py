#https://blog.csdn.net/zhizhengguan/article/details/126750993?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-126750993-blog-127418027.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-126750993-blog-127418027.pc_relevant_default&utm_relevant_index=6
def isValid(s) :
    if len(s) % 2 == 1:
        return False

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

        else:
            stack.append(ch)
        print(stack)

    return not stack


print(isValid("([])[]{}"))