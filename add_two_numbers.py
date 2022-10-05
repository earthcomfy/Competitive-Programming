"""
Add two numbers - Singly linked list: https://leetcode.com/problems/add-two-numbers/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        carry = 0
        ptr = res
        
        
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            total = num1 + num2 + carry
            carry, val = total // 10, total % 10
            
            ptr.next = ListNode(val)
            
            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return res.next

        
