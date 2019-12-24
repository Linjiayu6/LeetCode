"""
判断是否有环存在
3 -> 1 -> 4 -> 5 -> 
     ^-------------    

1. dict = {}
2. if cur.val in dict:
      dict[cur.val] += 1
   else:
      dict[cur.val] = 1
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
