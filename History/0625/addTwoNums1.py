class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNums (l1, l2):
        sum_data = l1.val + l2.val
        ll = ListNode(sum_data % 10)
        # 将进位值放到ll.next中
        ll.next = ListNode(sum_data // 10)

        p1 = l1.next
        p2 = l2.next
        p3 = ll

        while(True):
            if p1 and p2:
              sum_val = p1.val + p2.val + p3.next.val
              p3.next = ListNode(sum_data % 10)
              p3.next.next = ListNode(sum_val // 10)

              p1 = p1.next
              p2 = p2.next
              p3 = p3.next
            elif p1 and not p2:
              sum_val = p1.val + p3.next.val
              p1 = p1.next
              p3 = p3.next
            elif p2 and not p1:
              sum_val = p2.val + p3.next.val
              p2 = p2.next
              p3 = p3.next
            else:
              if p3.next.val == 0
                p3.next = None
              break
        return p3



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        res = head
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            tmp = num1 + num2 + carry
            carry = 1 if tmp >= 10 else 0
            head.next = ListNode(tmp % 10)
            head = head.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: head.next = ListNode(1)
        return res.next