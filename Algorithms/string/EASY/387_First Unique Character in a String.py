# https://leetcode-cn.com/problems/first-unique-character-in-a-string/
# 387. First Unique Character in a String

"""
s = "loveleetcode",
return 2.
"""
# excel the running time !!!
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        L = list(s)
        for i, d in enumerate(L):
            if L.count(d) == 1:
                return i
        return -1


# create hashTable and second time to iterate
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        
        _hashTable = {}
        for d in s:
            if d in _hashTable:
                _hashTable[d] += 1
            else:
                _hashTable[d] = 1
        for i, _d in enumerate(s):
            if _hashTable.get(_d) == 1:
                return i
        return -1