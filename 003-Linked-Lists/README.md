# Linked Lists

### Fast and Slow Pointers
Fast and slow pointers is an implementation of the two pointers technique that we learned in the arrays and strings chapter. The idea is to have two pointers that don't move side by side. This could mean they move at different "speeds" during iteration, begin iteration from different locations, or any other abstract difference.

```
function fn(head):
    slow = head
    fast = head

    while fast and fast.next:
        Do something here
        slow = slow.next
        fast = fast.next.next
```

The reason we need the while condition to also check for fast.next is because if fast is at the final node, then fast.next is null, and trying to access fast.next.next would result in an error (you would be doing null.next).

### The `Dummynode` Concept
A dummy node is a placeholder node added at the beginning of a linked list. It does not hold any meaningful data but serves as a sentinel to simplify edge case handling. Here are the key points about dummy nodes:

- **Simplifies Edge Cases:** In operations like deletion or insertion at the beginning of the list, handling edge cases can be tricky. A dummy node ensures that these operations do not require separate logic for the first element.
- **Uniformity in Logic:** With a dummy node, every element, including the first real node, has a node before it. This uniformity allows for consistent logic throughout the list traversal and manipulation, reducing the risk of errors.
- **Preserving the Head:** In some operations, the head of the list might change (e.g., deletion of the first node). A dummy node ensures that the head reference remains constant, as it always points to the dummy node.
Ease of Implementation: Implementing algorithms becomes more straightforward with a dummy node, as you can avoid multiple checks for null or special conditions for the head of the list.

### Maintaining a `prev` node
The prev pointer is used to keep track of the previous node in a traversal or manipulation of a linked list. Its utility is especially evident in operations where the linkage of nodes needs modification. Here’s how the prev pointer is useful:

- **Tracking the Previous Node:** In many linked list operations, such as deletion or rearrangement, knowing the node immediately preceding the current node is crucial. The prev pointer keeps this information readily available.
- **Modifying Links:** When you need to remove a node or rearrange nodes, the prev pointer helps in updating the next pointers correctly. For example, to remove a node, you set prev.next to node.next, effectively bypassing the node to be removed.
- **Backtracking:** In certain scenarios, like reversing a linked list or in some types of traversal, you might need to go back to a previous node. The prev pointer allows for this kind of backtracking.
