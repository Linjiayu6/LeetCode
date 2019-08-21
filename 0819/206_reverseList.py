# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.L = []

    def value(self, head):
        if head and head.val:
            self.L.append(head.val)
            # !!!
            head = head.next
            self.value(head)
        return self.L

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.L = self.value(head)
        node = ListNode(self.L[-1])
        for val in self.L[::-2]:
            node_new = ListNode(val)
            node_new = node.next
        return node