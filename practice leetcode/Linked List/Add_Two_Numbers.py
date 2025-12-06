# Solution thought on my own first draft

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        nextPointer = None
        carry = 0
        place = 1

        while l1 and l2:
            newNode = ListNode()
            newNode.next = nextPointer
            value = l1.value + l2.value + carry
            if value > 10:
                carry = (value // 10)% 10
                value = value % 10
            else:
                carry = 0
            newNode.val = value
            place += 1
        
        while l1:
            newNode = ListNode()
            newNode.next = nextPointer
            value = l1.value + carry
            if value > 10:
                carry = (value // 10)% 10
                value = value % 10
            else:
                carry = 0
            newNode.val = value
            place += 1
        while l2:
            newNode = ListNode()
            newNode.next = nextPointer
            value = l2.value + carry
            if value > 10:
                carry = (value // 10)% 10
                value = value % 10
            else:
                carry = 0
            newNode.val = value
            place += 1

