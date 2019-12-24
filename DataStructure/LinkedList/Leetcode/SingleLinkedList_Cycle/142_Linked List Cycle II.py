"""
判断是否有环存在, 在141题基础上需要返回该节点

3 -> 1 -> 4 -> 5 -> 
     ^-------------    
思路: 将整个node结点放入至字典中。
1. dict = {}
2. if cur in dict:
      return dict[cur]
   else:
      dict[cur] = 位置
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        _dict = {}

        if head is None:
            return None
        while head is not None:
            if head in _dict:
                return head
            # 位置存入
            _dict[head] = 1
            head = head.next
        return head