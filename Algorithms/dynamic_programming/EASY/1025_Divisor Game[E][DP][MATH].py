# -*- coding: utf-8 -*

"""
https://leetcode-cn.com/problems/divisor-game/

A 和 B 博弈, A开始, 指定N
Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
"""

"""
这个世界上无非是奇数或者偶数
奇数: 只有一种可能性, 最小情况是除以1, 可以除尽, 下一次为偶数
偶数: 两种可能, 最小的情况 1 或 2

if N 为奇:
  N = N - 1
if N 为偶数:
  N = N - 1 或 N - 2

B = 1
A = 2 
B = 3 或 4
...

有很多种情况, 但是如果让B一定输, 一定是给A偶数
....
"""

"""
思考一个问题, 如果让B输掉比赛, 那么最后一步是B拿到的值为1, 往前推, A要拿到的值是2
所以已经确定了, 如果要让B输掉比赛, 最后几步一定是该节奏。
数字: 无非是奇数或者偶数
奇数可以除的是奇数或1, 但是可以确定的是, 下一个数一定是偶数。 例如 9 % 3 = 0, 下一个数是9-3 = 6
偶数可以除的是奇偶数或1, A为先出一方, 只要保证给B的是个奇数, B就一定输。
"""

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0
        
"""
输定了系列, B一定是奇数1, A是2, B...
[占位, 输, 赢, 输, 赢, ...] = [False, F, T, F, T, ...]
自底向上求解
"""
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # 第一个false是占位
        L = [False, False, True] + [False] * (N - 2)
        if N < 3:
            return L[N]
        else:
            for i in range(3, N + 1):
                for j in range(1, i):
                    # 可以被整除, 且下一个状态是False, 说明让B输的状态
                    if i % j == 0 and L[i-j] == False:
                        L[i] = True
                        break
            print L
            return L[N]