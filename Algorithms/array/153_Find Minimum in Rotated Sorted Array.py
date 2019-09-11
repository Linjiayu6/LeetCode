# -*- coding: utf-8 -*
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.

Input: [3,4,5,1,2] 
Output: 1
"""
# class Solution(object):
#     def findMin(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1:
#             return nums[0]
        
#         for i in range(1, len(nums)):
#           if (nums[i-1] > nums[i]):
#               return nums[i]
#         return nums[0]
# print Solution().findMin([3,4,5,1,2])


"""
binary search algorithm 二分查找
- 中间取数据, 跟左右两边数比较
- 从左边group再取中间值, 重复上一步
- 直到数据为空为止
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        i, j = 0, _len - 1
        if _len == 1:
            return nums[0]

        while(j > i):
            print i, j
            if nums[i] < nums[i + 1]:
                i += 1
            else:
                return nums[i + 1]

            if nums[j] > nums[j - 1]:
                j -= 1
            else:
                return nums[j]

print Solution().findMin([3,4,5,1,2])

"""
或者直接找最小的
"""

# return min(nums)
