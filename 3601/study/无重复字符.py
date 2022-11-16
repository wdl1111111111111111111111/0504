class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        har = set()
        leftcur = 0
        rightcur = 0
        maxl = 0
        while leftcur < n:
            #判断没有重复，并向哈希表中添加字符
            while rightcur < n and s[rightcur] not in har:
                har.add(s[rightcur])
                rightcur = rightcur + 1
            #存在重复，读取最长长度
            maxl = max(maxl, rightcur-leftcur)
            #从左向右依次删除哈希表中字符，直到第二个while循环不再break为止
            har.remove(s[leftcur])
            leftcur = leftcur + 1
        return maxl

