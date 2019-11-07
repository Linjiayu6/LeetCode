"""
[9, 9]
=> [1, 0, 0]

拼接成字符串'99', 转int 99, 99 + 1
100, 转字符串, list(string)
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(str(int(''.join(map(str, digits))) + 1))

print Solution().plusOne([9,9])
