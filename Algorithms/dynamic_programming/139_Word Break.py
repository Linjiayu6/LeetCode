# -*- coding: utf-8 -*
"""
s = "applepenapple", wordDict = ["apple", "pen"]
s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
s = 'cars', wordDict = ["car","ca","rs"]

- 遍历wordDict, 每次s.replace(item, '')
- if len(s) === 0: return true
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        

print Solution().wordBreak("ccaccc", ["cc", 'ac'])
