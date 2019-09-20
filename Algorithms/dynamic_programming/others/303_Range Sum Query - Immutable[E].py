# -*- coding: utf-8 -*

# [1] 第一种
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])


# [第二种] 跟爬楼梯一样
"""
公式推导:
# i - j
# _sum = L[0: i] + L[i: j + 1] + L[j + 1: len(nums)]
# L[i: j + 1] = _sum -  L[0: i] - L[j + 1: len(nums)]
# L[i: j + 1] = _sum - L[0: i] - (_sum - L[0:j+1])
# L[i:j+1] = L[0:j+1] - L[0:i]
"""

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j+1] - self.nums[i]
