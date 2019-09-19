# -*- coding: utf-8 -*

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
"""

"""
1,2,5  = 11
C(11) = 1 + min(C(10), C(9), C(6))
C(10) = 1 + min(C(9), C(8), C(5))
...
"""

# 存到哈希表中
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 总金额为0
        if amount == 0:
            return 0
        # 最小纸币 都比 想要的值还要大, 肯定是没有的选择
        c_min = min(coins)
        if c_min > amount:
            return -1 

        # dictionary 存放从底至上的所有最小情况
        _dict = { c_min: 1 }
        for i in range(c_min + 1, amount + 1):
            # 存放当前最小值默认值为 -1(没有该值)
            temp_min = -1

            # 遍历所有纸币情况, 求最小值
            for d in coins:
                # 刚好有个纸币命中该值
                if i - d == 0:
                    temp_min = 0
                    break
                    
                elif i - d > 0:
                    # 先从_dict取数据
                    _dict_data = _dict.get(i - d)
                    # 有该值, 则比较取 当前最小值情况
                    if _dict_data >= 0:
                        # if temp_min != -1:
                        #     temp_min = _dict_data if temp_min > _dict_data else temp_min
                        # else:
                        #     temp_min = _dict_data
                        temp_min = min(_dict_data, temp_min) if temp_min != -1 else _dict_data

            _dict[i] = 1 + temp_min if temp_min != -1 else -1
        return _dict.get(amount)
        
print Solution().coinChange([2], 3)
