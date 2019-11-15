# https://leetcode-cn.com/problems/valid-anagram/
"""
Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 1. create hashTable
        _hashTable = {}
        for _s in s:
            if _s in _hashTable:
                _hashTable[_s] += 1
            else:
                _hashTable[_s] = 1
        # 2. all table keyList
        keyList = _hashTable.keys()

        tList = set(list(t))
        # 3. if length is not the same, return False
        if len(tList) != len(keyList):
            return False
        # 4. check all keyvalue
        for i in tList:
            # 5. t_key is not in keyList
            if i not in keyList:
                return False
            else:
                # 6. if count is not the same
                if t.count(i) != _hashTable[i]:
                    return False
        return True
        

print Solution().isAnagram('anmgram', 'nagaram')