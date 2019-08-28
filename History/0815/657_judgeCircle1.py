# -*- coding: utf-8 -*
"""
移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。
机器人的有效动作有 R（右），L（左），U（上）和 D（下）。
如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        RL, UD = 0, 0
        for i in moves:
            if i == 'R':
                RL += 1
            elif i == 'L':
                RL -= 1
            elif i == 'U':
                UD += 1
            elif i == 'D':
                UD -= 1

        return True if RL == 0 and UD == 0 else False
        
print Solution().judgeCircle('UD')