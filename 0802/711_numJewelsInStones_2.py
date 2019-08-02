# -*- coding: utf-8 -*

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(S.count(J_data) for J_data in J)


print Solution().numJewelsInStones('aA', 'aAABBCC')