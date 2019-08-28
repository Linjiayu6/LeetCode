
# quick

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}

        for i in nums:
            if i in dictionary:
                dictionary.pop(i)
            else:
                dictionary[i] = 1
        return dictionary.keys()[0]
