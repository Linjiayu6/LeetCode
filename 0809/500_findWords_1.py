
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        R = []
        s1, s2, s3 = 'eiopqrtuwy', 'adfghjkls', 'bcmnvxz'
        for i in words:
            j = set(i.lower())

            if j <= set(s1) or j <= set(s2) or j <= set(s3):
                R.append(i)
        return R
                             
print Solution().findWords(["asdfghjkl","qwertyuiop","zxcvbnm"])
