# -*- coding: utf-8 -*

"""
Your algorithm's runtime complexity must be in the order of O(log n).
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

# 双指针
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        if len(nums) == 1:
            return 0 if nums[0] == target  else -1

        while (i <= j):
          if nums[i] == target:
              return i
          if nums[j] == target:
              return j
          i += 1
          j -= 1
        return -1
