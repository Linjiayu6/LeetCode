class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count('R') == moves.count('L'):
            if moves.count('U') == moves.count('D'):
                return True

        return False
        # return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')
print Solution().judgeCircle('UD')