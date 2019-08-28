
# -*- coding: utf-8 -*

# 动态规划思想
# best 执行用时 :60 ms, 在所有 Python 提交中击败了92.59%的用户
class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)

print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])