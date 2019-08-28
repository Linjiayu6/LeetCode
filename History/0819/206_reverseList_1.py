# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# """
# 指针有head, j
#    1 -> 2 -> 3 -> null
# j  i head

#    2 -> 1 -> 3 -> null
# j  i   head

#    3 -> 2 -> 1 -> null
# j  i        head
# """

# class Solution(object):
#     def reverseList(self, head):
#         if head == None:
#             return None
#         else:
#             j = head
#             i = j
#             while head:
#                 j = ListNode(head.val)
#                 j.next = i
#                 head.next = head.next.next
                
#             return j