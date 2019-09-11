# -*- coding: utf-8 -*
"""
该题是1. 两数之和 的变形 给定 nums = [2, 7, 11, 15], target = 9
https://leetcode-cn.com/problems/two-sum/
思路是: 一次循环, 将值放入至dictionary中, 至到找到内容, 返回坐标值
"""
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Given array nums = [-1, 0, 1, 2, -1, -4],
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
(-1,0) { -1: [0,1] }
(-1,1) { 0: [0,2] }
(-1,2) { 1: [0,3] }
(-1,-1) { -2: [0,4] }
(-1,-4) { -5: [0,5] }
(0, 1) {1: [[0, 2], [1, 2]]}
...
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[inst]
        :rtype: List[List[int]]
        """
        # 缺少排序
        # nums = sorted(nums)
        if len(nums) < 3:
              return []
        i, j = 0, 1
        _dict = {}
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                data = nums[i] + nums[j]
                if _dict.get(data):
                    if _dict.get(data) != [[nums[i], nums[j]]]:
                        _dict[data] = _dict.get(data) + [[nums[i], nums[j]]]
                else:
                    _dict[data] = [[nums[i], nums[j]]]
                
                j += 1
            i += 1
        print _dict

        L, index = [], 0
        while index < len(nums) - 1:
            if _dict.get(-nums[index]):
                _prev = _dict.get(-nums[index]).pop(0)
                _next = nums[index]

                # 需要做一个过滤
                L += [_prev + [_next]]
            else:
                index += 1

        # 去重

        return L
print Solution().threeSum([-1, 0, 1, 2, -1, -4])


[
  [-1, 0, 1],
  [-1, -1, 2]
]

[[-1, 2, -1], [0, 1, -1], [2, -1, -1], [-1, 1, 0], [1, -1, 0], [-1, 0, 1], [0, -1, 1], [-1, -1, 2]]