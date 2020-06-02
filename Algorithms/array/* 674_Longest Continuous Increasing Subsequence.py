
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/

# continuous increasing subsequence
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1,3,5,4,7]
        # [2,2,2,2,2]

        if len(nums) == 0 or len(nums) == 1:
          return len(nums)
        _max = 1
        _temp = []
        for i in range(1, len(nums)):
          if nums[i] > nums[i - 1]:
            _max += 1
          else:
            _temp.append(_max)
            _max = 1
        
          if i == len(nums) - 1:
            _temp.append(_max)
        return max(_temp)

print(Solution().findLengthOfLCIS([1,3,5,6,7]))