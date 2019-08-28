
# -- coding:UTF-8 --

"""
344. 反转字符串
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while(i < j):
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return s


print Solution().reverseString(["h","e","l","l","o"])