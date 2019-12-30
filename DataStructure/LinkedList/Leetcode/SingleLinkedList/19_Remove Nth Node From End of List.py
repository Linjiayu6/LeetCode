# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Given a linked list, remove the n-th node from the end of list and return its head.

1. _len = all length
2. Node(_len - n) Node.next = Node.next.next
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or n == 0:
            return None

        _len, cur = 0, head
        while cur is not None:
            cur = cur.next
            _len += 1
        
        _no = _len - n
        # delete head
        if _no <= 0:
            head = head.next
        else:
            i, tempCur = 1, head
            while i < _no:
                tempCur = tempCur.next
                i += 1
            if n == 1:
                tempCur.next = None
            else:
                tempCur.next = tempCur.next.next
        return head