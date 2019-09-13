# -*- coding: utf-8 -*
"""
0 <= i <= 5
0 0000
1 0001
2 0010
3 0011
4 0100
5 0101

[0,1,1,2,1,2]

DP: 上一位的基础上, +1操作
"""
# class Solution(object):
#     def countBits(self, num):
#         """
#         :type num: int
#         :rtype: List[int]
#         """
#         L = [0]
#         for i in range(1, num + 1):
#             L.append(bin(i).count('1'))
#         return L

# print Solution().countBits(5)

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        """
        1: 001
        2: 010

        001 + 001
        - xor异或 + and操作 后 左移动运算符 << 1
        """
        L, xor, carry = [0], 0, 1
        while(xor < num):
          # 异或, 进位
          xor, carry = xor ^ carry, (xor & carry) << 1
          print xor, carry
          if (carry != 0): 
              xor += carry

          carry = 1
          L.append(bin(xor).count('1'))
        return L

print Solution().countBits(5)