class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        if len(array[0]) == 0:
            return False
        for i in range(len(array)):
            left = 0
            right = len(array[0])-1
            while left<=right:
                mid = (left+right)//2
                if array[i][mid]>target:
                    right = mid-1
                elif array[i][mid]<target:
                    left = mid+1
                elif array[i][mid]==target:
                    return True
        return False