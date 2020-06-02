#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""链表中间值, 并返回该链表"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def length (self, head):
#         count, cur = 0, head
#         while cur is not None:
#             count += 1
#             cur = cur.next
#         return count

#     def middleNode(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         # 为空, 则返回空
#         if head is None:
#             return None

#         len = self.length(head)
#         # 长度为1的时候, 直接返回head
#         if len == 1:
#             return head
#         # 其他情况
#         _count = len / 2
#         _index, cur = 1, head
#         """
#         1 -> 2 -> 3 -> None
#           len = 3, _count = 3 / 2 = 1 return cur.next
#         1 -> 2 -> 3 -> 4 -> None
#           len = 4, _count = 4 / 2 = 2 return cur.next
#         """
#         while _index < _count:
#             _index += 1
#             cur = cur.next
#         return cur.next



# [1,2,3,4,5,6]
"""
快慢指针
  count = 1 => slow = 1 fast = 1
  count = 2 => slow = 2 (2 / 2 + 1) fast = 2 
  count = 3 => slow = 2 (3 / 2) fast = 3
  count = 4 => slow = 3 (4 / 2 + 1) fast = 4
  count = 5 => slow = 3 (5 / 2) fast = 5
  count = 6 => slow = 4 (6 / 2) fast = 6
  偶数位数: slow 才走一位
  fast指针正常遍历
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        # 初始化
        slow, fast = head, head
        count = 1
        while (fast):
            # count为 偶数
            if count % 2 == 0:
                slow = slow.next
            fast = fast.next
            count += 1
            
        return slow


