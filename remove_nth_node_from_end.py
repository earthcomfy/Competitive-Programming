"""
Remove nth node: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
  
     
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = current2 = head
        
        while current:
            length += 1
            current = current.next
        
        if length == n:
            head = head.next
            return head
        
        while current2:
            if length == n+1:
                current2.next = current2.next.next
                break
            
            current2 = current2.next
            length -= 1
        
        return head
            
            
