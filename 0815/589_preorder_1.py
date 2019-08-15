# -*- coding: utf-8 -*

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def __init__(self):
        self.L = []
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        """
        1. node.val节点放入list中
        2. node.children 遍历孩子的节点
           node.children[0] ... [len-1]
           children[0].val插入L 
        3. 递归完成
        """
        if root != None:
            self.L.append(root.val)
            if len(root.children) != 0:
                for item in root.children:
                    # 递归自己调用自己的方法
                    self.preorder(item)
        else:
            return None

        return self.L



# 1744 ms, 在所有 Python 提交中击败了5.54%的用户


# 简单的写还是递归
class Solution(object):
    def __init__(self):
        self.L = []
    def preorder(self, root):
        if root != None:
            self.L.append(root.val)
            map(lambda i: self.preorder(i), root.children)
        else:
            return None
        return self.L