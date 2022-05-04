def two_sum(target,nums):
    dict_nums=dict()
    n = len(nums)
    for i in range(n):
        if target -nums[i] in dict_nums:
            return [dict_nums.get([target-nums[i]]),nums[i]]
        dict_nums[nums[i]]=input
        
    return []

target=56
nums=[1,2,3,7,6,9,34,23,43,28,24,22]
c=two_sum(target,nums)
print(c)