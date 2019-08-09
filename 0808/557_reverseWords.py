class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        List = s.split()
        L = []
        for i in List:
            L.append(i[::-1])
            
        return ' '.join(L)

print Solution().reverseWords("Let's take LeetCode contest")
