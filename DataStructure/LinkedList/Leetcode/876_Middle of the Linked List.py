#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def length (self, head):
        count, cur = 0, head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        len = self.length(head)
        if len / 2 == 0: