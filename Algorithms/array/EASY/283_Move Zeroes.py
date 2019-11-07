"""
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

list.remove(具体数)
[1,2,3,1]
list.remove(1) => 返回 [2,3,1]
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        _countzero = nums.count(0)
        for i in range(_countzero):
            nums.remove(0)
            nums.append(0)
        return nums