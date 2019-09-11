# -*- coding: utf-8 -*
"""
Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum

Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

- _max
- temp (save, contigious subarray data)
- current data
"""

# TODO: 可以继续的优化处理 v1
# class Solution(object):
#     def maxSubArray(self, nums):
#         temp = nums[0]
#         _max = temp
#         for i in range(1, len(nums)):
#             current = nums[i]
#             # _max 是存在目前最大值, 是不涉及到连续问题的, 因为只要最大值
#             _max = max(_max, current, current + temp, temp)
#             # 但是temp是一定要连续最大值
#             temp = max(current, current + temp)
#         return _max
# print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

# 可以继续优化 v2
# 数组nums[i-1] 存放最大值, 和 nums[i] 对比, 最后只要输出的是nums[i]就好了
class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)