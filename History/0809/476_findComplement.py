# -- coding:UTF-8 --

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        L = map(lambda i: '1' if i == '0' else '0', list(bin(num))[2:])
        return int(''.join(L), 2)

print Solution().findComplement(5)
