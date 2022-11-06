def search(list,target):
    if target in list:
        return list.index(target)
    elif target>list[-1]:
        return len(list)
    elif target<list[0]:
        return 0
    else:
        for s in list:
            if s>target:
                break
        return list.index(s)
print(search([1,3,5,6],7))