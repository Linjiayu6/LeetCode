# fast

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # math methods to calculate
        return 2 * sum(set(nums)) - sum(nums)
        