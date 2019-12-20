#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

(head)1 -> 0 -> 1 -> 1 -> 0 -> None
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if head is None:
            return 0
        
        L, cur = [], head
        while cur is not None:
            L.append(str(cur.val))
            cur = cur.next

        return int(''.join(L), 2)