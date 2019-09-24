"""
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2

[1, 3, 2, 8, 4, 9]
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        _lowest, result = prices[0], 0
        for i in range(1, len(prices)):
            # find lowest point
            if _lowest > prices[i]:
                _lowest = prices[i]
            # minus transaction fee
            elif _lowest < prices[i] - 2:
                result += prices[i] - _lowest - 2
                _lowest = prices[i]

        return result

print Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
