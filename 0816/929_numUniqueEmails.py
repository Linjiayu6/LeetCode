# -*- coding: utf-8 -*

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        S = set()
        for i in emails:
            L = i.split('@')
            first = L[0].split('+')[0]
            S.add(first.replace('.', '') + '@' + L[1])
        return len(S)

print Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])