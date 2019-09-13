# -*- coding: utf-8 -*
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bin(n) return string
        return bin(n).count('1')

print Solution().hammingWeight(00000000000000000000000000001011)
