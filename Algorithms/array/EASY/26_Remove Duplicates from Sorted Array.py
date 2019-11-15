# [0,0,1,1,1,2,2,3,3,4]
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if not nums:
            return 0
        else:
            k = 1
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1]:
                    nums[k] = nums[i]
                    k += 1
            return k