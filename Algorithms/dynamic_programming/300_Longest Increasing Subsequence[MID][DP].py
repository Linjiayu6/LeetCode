# -*- coding: utf-8 -*

"""
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4
"""

# 由下至上, 找规律, 其实跟爬楼梯一样的道理, 从小问题出发解决问题。

class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        _Store = [1] * len(nums)
        for i in range(1, len(nums)):
            _temp = 1
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    _temp = max(1 + _Store[j], _temp)
            _Store[i] = _temp
        return max(_Store)

# print Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6])



class Solution(object):
    def lengthOfLIS(self, nums):
        _len = len(nums)
        if _len == 0 or _len == 1:
            return _len
        else:
            _tempArr = [1] * _len
            for i in range(1, _len):
                for j in range(i - 1, -1, -1):
                    if nums[j] < nums[i]:
                        _tempArr[i] = max(_tempArr[j] + 1, _tempArr[i])
                        
        return max(_tempArr)