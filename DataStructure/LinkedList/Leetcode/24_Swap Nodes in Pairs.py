# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Given 1->2->3->4, you should return the list as 2->1->4->3.
思路:
1. 判断 cur = head, cur or cur.next 是否为空
2. if None, 结束返回
3. if is not None, 
   cur.val, cur.next.val = cur.next.val, cur.val
   cur = cur.next.next
"""

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur is not None:
            if cur.next is None:
                break
            else:
                cur.val, cur.next.val = cur.next.val, cur.val
                cur = cur.next.next

        
        