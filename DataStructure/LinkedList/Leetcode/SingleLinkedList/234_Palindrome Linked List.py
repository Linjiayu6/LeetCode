# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Input: 1->2->2->1
Output: true

Input: 1->2->2->2->2->1
Output: true
"""

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        List, i, j = [], 0, 0
        while head is not None:
            j += 1
            List.append(head.val)
            head = head.next
        j = j - 1
        while j > i:
            if List[i] == List[j]:
                i += 1
                j -= 1
            else:
                return False
        return True