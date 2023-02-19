import functools
from typing import List


class Solution:
    def compare(self, arr1: List[int], arr2: List[int]) -> int:  # 自定义比较两个列表的方法
        r1 = 1.0 * arr1[1] / arr1[0]
        r2 = 1.0 * arr2[1] / arr2[0]
        diffR = int(r2 - r1)
       # print(diffR)
        if diffR == 0:
            print("1111111111:",arr1[0] - arr2[0])
            return arr1[0] - arr2[0]
        return diffR

    def func(self, jobs: List[List[int]], T: int) -> int:
        result = 0
        # 自定义的方法对jobs列表进行排序
        jobs = sorted(jobs, key=functools.cmp_to_key(self.compare))
        print(jobs)
        sumTime = 0
        for job in jobs:
            if job[0] + sumTime > T:
                continue
            sumTime += job[0]
            result += job[1]
        return result


def inputParams():
    params = [int(x) for x in input().split(" ")]
    T = params[0]
    n = params[1]
    vector = []
    for i in range(n):
        temp = list(map(int, input().split()))
        vector.append(temp)
    object = Solution()
    res = object.func(vector, T)
    print(res)


if __name__ == "__main__":
    while 1:
        try:
            inputParams()
        except Exception as e:
            break