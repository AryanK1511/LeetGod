# Example 1: Given a string s, return true if it is a palindrome, false otherwise.
def check_is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(check_is_palindrome("abcdef"))
print(check_is_palindrome("abcdcba"))
print("===========")

# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

def check_sum_is_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    return False

print(check_sum_is_target([1, 2, 4, 6, 8, 9, 14, 15], 13))
print("===========")

# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

def combine_sorted_arrays(arr1, arr2):
    arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr.append(arr2[j])
        j += 1

    return arr

print(combine_sorted_arrays([1, 4, 7, 20], [3, 5, 6]))
print("===========")

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

def is_subsequence(s, t):
    s_ptr, t_ptr = 0, 0
    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1

    return  s_ptr == len(s)
            

print(is_subsequence("ace", "abcde"))
print(is_subsequence("aec", "abcde"))
print("===========")

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        
    return s

s = ["H", "E", "L", "L", "O"]
print(reverse_string(s))
print("===========")

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def square_sorted_array_1(nums):
    result = []
    left = 0
    right = len(nums) - 1

    while left <= right:
        square = 0
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right] * nums[right]
            right -= 1
        else:
            square = nums[left] * nums[left]
            left += 1
        result.insert(0, square)

    return result

# Faster Solution O(n) instead of O(n^2)
def square_sorted_array_2(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result

nums = [-4,-1,0,3,10]
print(square_sorted_array_2(nums))