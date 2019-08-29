"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

链接：https://leetcode-cn.com/problems/two-sum

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _dict = {}
        for indice, value in enumerate(nums):
            # not None: Must Dedicate
            if _dict.get(target - value) is not None:
                return [_dict.get(target - value), indice]
            _dict[value] = indice