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