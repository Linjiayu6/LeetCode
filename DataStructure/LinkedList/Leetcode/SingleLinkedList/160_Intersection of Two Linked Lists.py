"""
https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
160. Intersection of Two Linked Lists
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        Obj = {}
        while headA is not None:
            Obj[headA] = True
            headA = headA.next
        while headB is not None:
            if headB in Obj:
                return headB
            headB = headB.next
        return None
                