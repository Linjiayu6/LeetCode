# -*- coding: utf-8 -*

"""
给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

链接：https://leetcode-cn.com/problems/jewels-and-stones
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # 这种方式是错的, 会直接报错, 这总方式无法将string按照字母区分开来
        # J_list = J.split()
        # S_list = S.split()

        # 将字符串拆分为字符数组
        J_list, S_list = list(J), list(S)
        print J_list, S_list

        sum = 0
        # for j_data in J_list:
        #     for s_data in S_list:
        #         if j_data == s_data:
        #             sum = sum + 1
        # return sum

        # list.count(target)
        for j_data in J_list:
            sum = sum + S_list.count(j_data)
        return sum

print Solution().numJewelsInStones('aA', 'aAABBCC')