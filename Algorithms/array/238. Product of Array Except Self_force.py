# exceed time limit
class Solution(object):
    def multiply(self, x, y):
        return x * y

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = []
        for i, val in enumerate(nums):
            _L = nums[0: i] + nums[i+1:]
            L.append(reduce(self.multiply, _L))
        return L

print Solution().productExceptSelf([1,2,3,4])

"""
TEST DATA:
[1,0] -> [0, 1]
[0,0] -> [0, 0]

Input:  [1,2,3,4]
Output: [24,12,8,6]
"""


