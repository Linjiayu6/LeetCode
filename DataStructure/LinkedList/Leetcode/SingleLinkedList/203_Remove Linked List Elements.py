# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        cur = head
        # head.val head = head.next
        if head.val == val:
            head = head.next
            # 例如 [6,6,6] 6
            return self.removeElements(head, val)

        while cur is not None:
            if cur.next is not None and cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


# 头建立一个空结点。
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        # xx建一个虚拟 => 6 -> 1 -> 6 -> None
        tempNode = ListNode(0)
        tempNode.next = head

        cur = tempNode
        while cur.next is not None:
            if cur.next and cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return tempNode.next