class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        _len = len(nums)
        if _len == 0:
          return 0
        
        # 边界判断
        if nums[0] >= target:
          return 0

        if nums[_len - 1] < target:
          return _len
        
        if nums[_len - 1] == target:
          return _len - 1

        i = 1
        while (i < _len):
          if nums[i] >= target and nums[i - 1] < target:
            return i

          i += 1