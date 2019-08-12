# -*- coding: utf-8 -*

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入: [-2,1,-3,4,-1,2,1,-5,4]

- 保证局部最小
从index=0开始, 两个相加
(-1 1 1 -4 4)
- 0 -3 4
- -1 2 0
从index=1开始, index = 0空出来的, 两个相加
(-2 -2 3 3 -1)
- -4 6 -1
- -2 1 2
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        Dict = dict()
        nums_len = len(nums) - 1

        while(i < nums_len):
            if i + 1 == nums_len:
                Dict[(i)] = nums[i]
            else:
                Dict[(i,i+1)] = nums[i] + nums[i+1]
                i += 2
        print Dict

Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])