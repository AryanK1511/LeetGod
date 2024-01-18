# Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False

# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
        
        # If fast is None, we need to remove the head
        if not fast:
            return head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head