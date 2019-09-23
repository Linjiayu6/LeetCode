"""
[5,3,4,5]

value = _prev + max(L[0], L[-1])
A: first to get data
"""
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        i, j = 0, len(piles) - 1
        A, B = 0, 0
        while i < j:
            # L[i], L[j]
            # give A max data
            if piles[i] > piles[j]:
                A += piles[i]
                i += 1
                # for B
                if piles[i] > piles[j]:
                    B += piles[j]
                    j -= 1
                else:
                    B += piles[i]
                    i += 1
            else:
                A += piles[j]
                j -= 1

                # for B
                if piles[i] > piles[j]:
                    B += piles[j]
                    j -= 1
                else:
                    B += piles[i]
                    i += 1
        return A > B

print Solution().stoneGame([1, 5])