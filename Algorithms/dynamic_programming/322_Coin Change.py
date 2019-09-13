"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
"""

"""
1,2,5

多少种情况
[1] 1 = (1)
[2] [1] + 1; 2 = (2)
[3] [2] + 1; [1] + [1] + [1] = (3)
[4] [3] + 1; [2] + 2; [1] * 4 = (6)
[5] [4] + [3] + [2] + [1] + 5 = (13)
[6] [5] + [4] + [3] + [2] + [1] = (39)

fn = fn-1 + fn-2 + fn-3 + ... + 1
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        count = 0
        temp = coins[-1]
        if temp > amount:
            coins.pop(-1)
        else:
            temp = coins[-1]
            coins % temp