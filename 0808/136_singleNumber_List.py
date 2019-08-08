# slow

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        L = []
        for i in nums:
            if i not in L:
                L.append(i)
            else:
                L.remove(i)
        return L[0]