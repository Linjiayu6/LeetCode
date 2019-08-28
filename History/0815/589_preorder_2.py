# -*- coding: utf-8 -*

"""
非递归方法
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        # 每次stack以pop的方法
        Stack = [root]
        L = []
        # while len(Stack) != 0:
        while Stack:
            # 每次都pop()出去
            node = Stack.pop()
            if node != None:  
                L.append(node.val)
                # 此时[child4, child3, child2, child1] 逆序输出
                # 先处理的是child1, child1 可能还有children
                for child in node.children[::-1]:
                    Stack.append(child)
        return L