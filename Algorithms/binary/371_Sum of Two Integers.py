# -*- coding: utf-8 -*

"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
https://leetcode-cn.com/problems/sum-of-two-integers
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        xor = a ^ b
        carry = (a & b) << 1
        # xor + carry 才是最终的答案
        if carry != 0:
            return self.getSum(xor, carry)
        return xor

print Solution().getSum(-1200, 1)

"""
1: 0b1
2: 0b10
-2: -0b10

[1. XOR, 相同为0, 不同为1]
0 + 0 = 0
1 + 0 = 1
0 + 1 = 1
1 + 1 = 0 (carry 1)

不考虑进位问题, 其实是个异或XOR的运算, 相同为0, 不同为1
python: a ^ b 

[2. 与运算, 进位, 都是1才是1, 其余都是0]
a = 5 = 0101
b = 4 = 0100

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1

进位(与操作)是:
0101
0100
-----
0100
但是需要注意的是, 要在后面多补充一位 << 1运算

[3. 二进制补位] 左移动运算符, 右移动运算符
a = 0011 1100
a << 1 = 0111 1000
a << 2 = 1111 0000

a >> 2 = 0000 1111
"""