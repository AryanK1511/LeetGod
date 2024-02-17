# Creating a singly linked list
class SinglyLinkedList:
    class Node:
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next
    
    def __init__(self, value=None):
        # Initialize head as None if no value is provided
        if value is None:
            self.head = None
        else:
            self.head = self.Node(value)

    def insert_beginning(self, value=0):
        new_node = self.Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

sll1 = SinglyLinkedList()
sll1.insert_beginning(5)
sll1.insert_beginning(4)
sll1.insert_beginning(4)
sll1.insert_beginning(3)
sll1.insert_beginning(3)
sll1.insert_beginning(2)
sll1.insert_beginning(1)
print("ORIGINAL")
sll1.print_list()
print("MODIFIED")
