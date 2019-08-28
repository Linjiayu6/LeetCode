class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = 0
        for i in str(num):
            s += int(i)
        return self.addDigits(s) if len(str(s)) > 1 else s
        