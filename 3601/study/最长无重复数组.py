class Solution:
    def maxLength(self, arr:List[int]) -> int:
        # write code here
        l, r = 0, 0
        hashmap = {}
        result = 0
        if len(arr) < 2:
            return len(arr)
        else:
            while r < len(arr):
                if arr[r] not in hashmap:
                    hashmap[arr[r]] = r
                    result = max(result, r - l + 1)
                    r += 1
                else:
                    l = max(hashmap[arr[r]] + 1, l)
                    hashmap[arr[r]] = r
                    result = max(result, r - l + 1)
                    r += 1
            return result