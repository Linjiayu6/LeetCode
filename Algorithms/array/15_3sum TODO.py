# -*- coding: utf-8 -*

# [-1, 0, 1, 2, -1, -4]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        List = []
        
        # 1. 排序
        nums = sorted(nums)
        
        # 2. 双指针
        _len = len(nums)
        for p in range(0, len(nums) - 2):
            _2sum = 0 - nums[p]

            for i in range(p + 1, len(nums) - 1):
                for j in range(p + 2, len(nums)):
                    if nums[i] + nums[j] == _2sum:
                        List.append([nums[p], nums[i], nums[j]])
        
        return List