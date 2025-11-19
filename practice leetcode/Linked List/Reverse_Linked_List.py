# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
            if not head:
                 return None
            new_Head = head

            if head.next:
                 new_Head = self.reverseList(head.next)
                 head.next.next = head
            head.next = None
            
            return new_Head