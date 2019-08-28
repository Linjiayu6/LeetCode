# -*- coding: utf-8 -*

# ascii_lowercase: abcdefghijklmnopqrstuvwxyz
from string import ascii_lowercase

List = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
WordList = list(ascii_lowercase)

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        L = []
        for w in words:
            L_item = ''
            for i in list(w):
                # WordList
                L_item = L_item + List[WordList.index(i)]
            L.append(L_item)
        return len(set(L))

print Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
