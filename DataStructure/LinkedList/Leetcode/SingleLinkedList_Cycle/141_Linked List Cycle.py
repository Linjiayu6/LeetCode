"""
判断是否有环存在
3 -> 1 -> 4 -> 5 -> 
     ^-------------    
思路: 将整个node结点放入至字典中。
1. dict = {}
2. if cur in dict:
      return True
   else:
      dict[cur] = 1
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        cur = head
        _dict = {}
        while cur is not None:
            if cur in _dict:
                return True
            _dict[cur] = 1
            cur = cur.next
        return False


"""
思路: 快慢双指针, 能相遇则为True, 相遇不了则为False
图解: https://leetcode-cn.com/problems/linked-list-cycle/solution/dong-hua-yan-shi-141-huan-xing-lian-biao-by-user74/
"""
class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        quick, slow = head, head
        while True:
            # 快指针需要优先判断是否有空
            quick = quick.next
            if quick is None:
                return False
            # 快指针需要优先判断是否有空
            quick = quick.next
            if quick is None:
                return False

            slow = slow.next
            # 指针相遇
            if quick == slow:
                return True
        return False