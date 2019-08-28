# -*- coding: utf-8 -*

"""
[链表]
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
(1) 某一个链表是空;
(2) 进位问题; (例如 7 + 9 = 16, 1是进位, 6是保留在链表中的)
(3) 最后一位溢出问题;

!!!链表是有一个表头的
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 直接对两个链表操作；对应节点上的值做加法运算，过10则进位。位数不够则补0
    def addTwoNumbers(self, l1, l2):
        # 链表头, ll可以理解为当前链表指针位置
        head = ListNode(0)
        # 当前指针位置
        ll = head

        # flag
        flag = 0
        while l1 or l2:
          l1_val = l1.val if l1 else 0
          l2_val = l2.val if l1 else 0
          sum_data = l1_val + l2_val + flag
          
          # 不需要补位
          if sum_data < 10:
            flag = 0
          # 需要补位
          else:
            flag = sum_data / 10
            sum_data = sum_data % 10

          # node: ListNode 一个结点
          node = ListNode(sum_data)
          # 指向node结点
          ll.next = node
          # 指针位置移动
          ll = ll.next
          
          l1 = l1.next if l1 else None
          l2 = l2.next if l2 else None
          

        return ll



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 从带个数据开始, 当前指针指向的都是第一个位
        n = l1.val + l2.val
        # 创建新node
        l3 = ListNode(n % 10)
        # next位置是 多余的进位数
        l3.next = ListNode(n // 10)
        # 指针移动
        p1 = l1.next
        p2 = l2.next
        # 开始指针还是p3
        p3 = l3

        while True:
            if p1 and p2:
                sum = p1.val + p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p2 = p2.next
                p3 = p3.next
            elif p1 and not p2:
                sum = p1.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p3 = p3.next
            elif not p1 and p2:
                sum = p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p2 = p2.next
                p3 = p3.next
            else:
                if p3.next.val == 0:
                    p3.next = None
                break
        return l3