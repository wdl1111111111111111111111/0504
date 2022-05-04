def paint_nums(s):
    """
    每次遍历所有元素，并移除所有能被第一个元素整除的元素
    :param s:
    :return:
    """
    arr = [int(x) for x in s.split(" ")]
    arr.sort()
    l = len(arr)
    i = 0
    start = arr[0]
    color = 1
    while arr:
        if i > l - 1:
            i = 0
            color += 1  # 每轮遍历完，颜色加一
            start = arr[i]
        elif arr[i] % start == 0:
            arr.pop(i)        
            l -= 1
            print("arr:i:",arr,start,i,l)
        else:
            i += 1
    return color
 
 
print(paint_nums("2 3 4 9"))
