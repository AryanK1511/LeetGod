# Reverse a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev


# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# class Solution:
#     def reverseBetween(self, head, left, right):
#         prev = None

#         while head.val != left:
#             prev = head
#             head = head.next

#         while head.val != right:
#             next_node = head.next
#             head.next = prev
#             prev = head
#             head = next_node