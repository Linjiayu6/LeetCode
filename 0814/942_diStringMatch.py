# -*- coding: utf-8 -*
"""
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有:
如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]
链接：https://leetcode-cn.com/problems/di-string-match
"""

"""
双指针i(从最小数开始递增), j(从最大数开始递减)
I: 从小的数开始
D: 从最大值开始
"""

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left, right, L = 0, len(S), []
        for i in S:
            if i == 'I':
                L.append(left)
                left += 1
            else:
                L.append(right)
                right -= 1
        # 剩下的值无论是left 或 right都是可以满足条件的
        return L + [left]

print Solution().diStringMatch("IDD")
