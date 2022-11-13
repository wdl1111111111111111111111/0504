def test(array):
    s=list(set(array))
    new_array=[]
    for i in s:
        if array.cout(i)==1:
            new_array.append(i)
    for i in range(2):
        if array[0]>array[1]:
            new_array[0],new_array[1]=new_array[1],new_array[0]
    return new_array