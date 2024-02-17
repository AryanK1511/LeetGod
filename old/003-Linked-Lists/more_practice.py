from test_linked_list import sll1

# Delete the middle node of a linked list
def deleteMiddle(head):
    if head is None or head.next is None:
        return None

    slow = fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    prev.next = slow.next
    slow.next = None

    return head

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
def remove_duplicates(head):
    if head is None:
        return None

    dummy_node = ListNode(0)
    dummy_node.next = head
    prev = dummy_node

    while head:
        if head.next and head.next.val == head.val:
            while head.next and head.next.val == head.val:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next

        head = head.next

    return dummy_node.next