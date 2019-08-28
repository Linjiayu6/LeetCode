
# quick

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = sorted(nums)
        i = 0
        while True:
            if i == len(L) - 1:
                return L[i]
            if L[i] == L[i+1]:
                i += 2
            else:
                return L[i]
        
print Solution().singleNumber([4,1,2,1,2])
