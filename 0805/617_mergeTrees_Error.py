# -*- coding: utf-8 -*

"""
# 合并二叉树
https://leetcode-cn.com/problems/merge-two-binary-trees/
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

数案例
t1: [1,3,2,5]
t2: [2,1,3,null,4,null,7]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 数的深度及节点个数
        t1_len, t2_len = len(t1), len(t2)
        L = []
        min_len = min(t1_len, t2_len)
        for i in range(min_len):
            if t1[i] and t2[i]:
                L.append(t1[i] + t2[i])
            else: 
                L.append(t1[i] or t2[i])
        if t1_len == min_len:
            L = L + t2[t1_len:]
        else:
            L = L + t1[t2_len:]
        return L

print Solution().mergeTrees([1,3,2,5], [2,1,3,None,4,None,7])
