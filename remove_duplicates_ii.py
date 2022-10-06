"""
Remove duplicates from sorted singly linked list: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        fast, slow = head, res
        
        while fast:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow, fast = slow.next, fast.next
            else:
                slow.next = fast.next
                fast = slow.next
                
        return res.next
