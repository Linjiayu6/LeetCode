# -*- coding: utf-8 -*

# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

# break是跳出整体循环; pass是跳出本次循环

class Solution(object):
    def onNew(self, L):
        new_L = []
        for val in L:
            if val != '#':
                new_L.append(val)
            else:
                if len(new_L) != 0:
                    new_L.pop()

        return new_L
                
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        new_S = self.onNew(S)
        new_T = self.onNew(T)
        print new_S, new_T

        return new_S == new_T