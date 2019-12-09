"""
237. Delete Node in a Linked List
https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
"""

"""
删除链表中某个值
eg: 1 -> 2 -> 3  删除2, 用3的node结点覆盖掉2的node就ok了。
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        