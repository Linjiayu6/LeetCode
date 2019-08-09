
class Solution(object):
    def select (self, j_first):
        s1, s2, s3 = 'eiopqrtuwy', 'adfghjkls', 'bcmnvxz'
        if j_first in s1:
            return s1
        elif j_first in s2:
            return s2
        else:
            return s3

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        R = []
        for i in words:
            j = list(set(i.lower()))
            # first one  j[0:1] is list
            j_first = j[0]
            rule = self.select(j_first)

            flag = True
            for char_j in j:
                if char_j not in rule:
                    flag = False
                    break
            if flag == True:
                R.append(i)
        return R
                             
print Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])

print set('as') < set('adfghjkls')