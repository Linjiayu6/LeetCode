# https://leetcode-cn.com/problems/same-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        


"""
递归, 这种方式会将树所有结点均遍历一遍
1. root is not None
   p.val == q.val: 递归p的左右子树
   return 继续递归输出 p.left, q.left 和 p.right, q.right

2. 均为空为返回 True
3. else 不满足条件返回 False
"""


# 迭代
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            # 结点 继续
            if not p and not q:
                continue
            # 值相同 继续
            if p and q:
                if p.val == q.val:
                    stack.append((p.left, q.left))
                    stack.append((p.right, q.right))
                else:
                    return False
            # 但凡有一个不同
            if p is None or q is None:
                return False
        return True


"""
1. 需要将p,q结点放入至数组里面
2. (p.left, q.left), (p.right, q.right) 同步对出现放入至数组中
3. 有不相同的情况就可以直接返回False, 其实不需要遍历所有结点

36 ms, 在所有 python3 提交中击败了95.56%的用户
"""