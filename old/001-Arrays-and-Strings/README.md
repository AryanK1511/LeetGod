# General Pattern in Questions

## Pattern 1
If its a subarray problem which has contrints such as:
- Sum greater than or less than k
- Limits on what is contained, such as the maximum of k unique elements or no duplicates allowed

And/or asks for:
- Minimum or maximum length
- Number of subarrays/substrings
- Max or minimum sum

> The problems above can usually be solved by using **Sliding Window**

## Pattern 2
If a problem's input is an integer array and you find yourself needing to calculate multiple subarray sums, consider building a **prefix sum**.

## Quick Tips
The size of a subarray between `i` and `j` (inclusive) is `j - i + 1`. This is also the number of subarrays that end at `j`, starting from `i` or later.

## Definitions

- **Subarrays / Substrings:** A subarray or substring is a contiguous section of an array or string.
- **Subsequences:** A subsequence is a set of elements of an array/string that keeps the same relative order but doesn't need to be contiguous.

> For example, subsequences of [1, 2, 3, 4] include: [1, 3], [4], [], [2, 3], but not [3, 2], [5], [4, 1].

- **Subsets:** A subset is any set of elements from the original array or string. The order doesn't matter and neither do the elements being beside each other. For example, given [1, 2, 3, 4], all of these are subsets: [3, 2], [4, 1, 2], [1]. Note: subsets that contain the same elements are considered the same, so [1, 2, 4] is the same subset as [4, 1, 2].

## Personal tips that I learnt
- If you are trying to find the prefix sum between two points `i` and `j`. There can be two formulae:
    1. If you are including `i`, the formula is `prefix_sum_arr[i] - prefix_sum_arr[j] + arr[i]`.
    2. If you are not including `i`, the formula is `prefix_sum[i] - prefix_sum[j]`
- In sliding window, you do not always need a whole array to track things, you can slide the window in programs that require summation for example by just subtracting from the left and adding to the right. You do not need an array to do this.
- Formula to calculate the length of a window is: `right_pointer - left_pointer + 1`

## What does Amortized Time Complexity mean?
Amortized analysis is a method used in computer science to find an average running time per operation over a sequence of operations, even though a single operation within the sequence might have a worst-case running time. In simpler terms, it's a way to average out the cost of expensive operations over many cheap ones. The term "amortized O(n)" means that over a series of n operations, the average time per operation is O(n), even if some individual operations may take longer.

One classic example of amortized analysis is the dynamic array, often seen in the form of Python's list or Java's ArrayList.