class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

head = n1
curr = head

while curr:
    print("Curr: ", curr.val)
    print("Head: ", head.val)
    curr = curr.next