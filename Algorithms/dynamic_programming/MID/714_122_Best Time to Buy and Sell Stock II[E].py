"""
贪心算法: 
Input: [7,1,5,3,6,4]
Output: 7

[-6, 4, -3, 3, -2]

Input: [1,2,3,4,5]
Output: 4
"""

# 122. 买卖股票的最佳时机 II 作为714题的基础题
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                result += prices[i] - prices[i-1]
        return result

print Solution().maxProfit([1,2,3,4,5])
