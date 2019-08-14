# -*- coding: utf-8 -*

# 其实该方法和 53_maxSubArray_1.py差不多, max的判断反而会影响执行时间
class Solution(object):
    def maxSubArray(self, nums):
        # 前一个值 或 前一组连续的值
        tmp = nums[0]
        max_ = tmp
        for i in range(1, len(nums)):
            max_ = max(tmp + nums[i], max_, tmp, nums[i])
            tmp = max(tmp + nums[i], nums[i])
        return max_

print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
