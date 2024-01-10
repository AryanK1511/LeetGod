# General Pattern in Questions

## Pattern 1
If its a subarray problem which has contrints such as
- Sum greater than or less than k
- Limits on what is contained, such as the maximum of k unique elements or no duplicates allowed

And/or asks for:
- Minimum or maximum length
- Number of subarrays/substrings
- Max or minimum sum

> The problems above can usually be solved by using **Sliding Window**

## Pattern 2
If a problem's input is an integer array and you find yourself needing to calculate multiple subarray sums, consider building a prefix sum.

## Quick Tips
- The size of a subarray between i and j (inclusive) is j - i + 1. This is also the number of subarrays that end at j, starting from i or later.

## Definitions

#### Subarrays / Substrings
a subarray or substring is a contiguous section of an array or string.

#### Subsequences
A subsequence is a set of elements of an array/string that keeps the same relative order but doesn't need to be contiguous.

> For example, subsequences of [1, 2, 3, 4] include: [1, 3], [4], [], [2, 3], but not [3, 2], [5], [4, 1].

#### Subsets
A subset is any set of elements from the original array or string. The order doesn't matter and neither do the elements being beside each other. For example, given [1, 2, 3, 4], all of these are subsets: [3, 2], [4, 1, 2], [1]. Note: subsets that contain the same elements are considered the same, so [1, 2, 4] is the same subset as [4, 1, 2].

## Personal tips that I learnt
- If you are trying to find the prefix sum between two points `i` and `j`. There can be two formulae:
    1. If you are including `i`, the formula is `prefix_sum_arr[i] - prefix_sum_arr[j] + arr[i]`.
    2. If you are not including `i`, the formula is `prefix_sum[i] - prefix_sum[j]`
- In sliding window, you do not always need a whole array to track things, you can slide the window in programs that require summation for example by just subtracting from the left and adding to the right. You do not need an array to do this.

## What does Amortized Time Complexity mean?
Amortized analysis is a method used in computer science to find an average running time per operation over a sequence of operations, even though a single operation within the sequence might have a worst-case running time. In simpler terms, it's a way to average out the cost of expensive operations over many cheap ones. The term "amortized O(n)" means that over a series of n operations, the average time per operation is O(n), even if some individual operations may take longer.

One classic example of amortized analysis is the dynamic array, often seen in the form of Python's list or Java's ArrayList.

**Dynamic Array Example:**

A dynamic array is an array that grows automatically when you try to insert an element and there's no more space left. Here's how it generally works:

- **Initial Allocation:** It starts with an initial capacity (let's say 1 for simplicity).
- **Adding an Element:** When you add an element, if there's enough space, it's an O(1) operation (constant time).
- **Exceeding Capacity:** When the array's capacity is exceeded, it needs to expand. It usually doubles its size.
- **Doubling Process:** To double the array, a new array of twice the size is allocated, and all elements are copied from the old array to the new one. This operation is O(n), where n is the number of elements in the array.

At first glance, it might seem like adding an element can sometimes be O(n), which would be bad if you're adding elements frequently. However, this is where amortized analysis comes in.

**Amortized Analysis of Dynamic Array:**

- **Doubling Less Frequent:** Each time the array doubles, it gets significantly bigger, meaning that the next doubling operation will happen after a lot more O(1) additions.
- **Spreading the Cost:** The cost of one O(n) doubling operation is spread out (or amortized) over the many O(1) additions that happened before it needed to double.

If you add up all the operations (including the expensive doubling ones) and average them out, the time per operation is O(1) on an amortized basis. This means that for a large number of operations, the average time per operation is constant.

In summary, while a dynamic array might occasionally have to perform an expensive resizing operation, when considered over a large number of operations, the average cost per operation remains constant, and this is what is meant by amortized O(1) complexity.