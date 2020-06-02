
# [1,2,4,3,5,4,7,2]
# 不连续 的最长子序列的个数
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        if _len == 0 or _len == 1:
            return _len
        
