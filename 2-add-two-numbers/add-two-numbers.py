# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resp = ListNode()
        resp_tracker = resp
        carry = 0
        while l1 or l2 or carry:
            sum_temp = 0
            if l1:
                sum_temp = sum_temp + l1.val
                l1 = l1.next
            if l2:
                sum_temp = sum_temp + l2.val
                l2 = l2.next
            if carry:
                sum_temp = sum_temp + carry
            
            carry = sum_temp // 10
            
            resp.next = ListNode(sum_temp % 10)
            resp = resp.next
        
        return resp_tracker.next




        