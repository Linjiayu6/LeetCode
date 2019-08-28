# -*- coding: utf-8 -*

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
        D = {}
        for i in cpdomains:
            # 次数, 字符串
            count, string = i.split()
            seqL = []
            for j in string.split('.')[::-1]:
                # 在特定的位置上插入数据
                seqL.insert(0, j)
                seqStr = '.'.join(seqL)

                if seqStr in D:
                    D[seqStr] += int(count)
                else:
                    D[seqStr] = int(count)
        L = []
        for key, value in D.items():
            L.append(str(value) + ' ' + key)
        return L

# ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
print Solution().subdomainVisits(["9001 discuss.leetcode.com"])
