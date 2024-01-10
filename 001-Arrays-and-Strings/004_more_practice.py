# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
def reverse_words(s):
    return " ".join([word[::-1] for word in s.split(" ")])

s = "Let's take LeetCode contest"
print(reverse_words(s))
print("============")

# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

def reverse_only_letters(s):
    s_arr = list(s)
    left, right = 0, len(s_arr) - 1

    while left < right:
        if not s_arr[left].isalpha():
            left += 1
        elif not s_arr[right].isalpha():
            right -= 1
        else:
            s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
            left += 1
            right -= 1
    return "".join(s_arr)

s = "a-bC-dEf-ghIj"
print(reverse_only_letters(s))
print("============")

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def move_zeroes(nums):
    i = 0  
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

nums = [1, 0]
print(move_zeroes(nums))
print("============")

# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

def prefix_reverse(word, ch):
    word_list = list(word)
    left = 0
    right = 0
    if ch not in word_list:
        return word
    else:
        while word_list[right] != ch:
            right += 1
    while left < right:
        word_list[left], word_list[right] = word_list[right], word_list[left]
        left += 1
        right -= 1
    return "".join(word_list)

word = "abcdefd"
ch = "d"

print(prefix_reverse(word, ch))
print("============")

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

def min_sub_arr_len(nums, target):
    left, sum, min_window = 0, 0, len(nums) + 1

    for right in range(len(nums)):
        sum += nums[right]
        while sum >= target:
            min_window = min(min_window, right - left + 1)
            sum -= nums[left]
            left += 1
    return min_window if min_window != len(nums) + 1 else 0

target = 7
nums = [2, 3, 1, 2, 4, 3]
print(min_sub_arr_len(nums, target))
print("============")

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

def max_num_of_vowels(s, k):
    left, v_count = 0, 0
    vowels = set(["a", "e", "i", "o", "u"])

    for right in range(k):
        if s[right].lower() in vowels:
            v_count += 1
    max_v_count = v_count

    for right in range(k, len(s)):
        if s[right].lower() in vowels:
            v_count += 1
        if s[left].lower() in vowels:
            v_count -= 1
        left += 1
        max_v_count = max(max_v_count, v_count)

    return max_v_count

s = "leetcode"
k = 3
print(max_num_of_vowels(s, k))
print("============")

# You are given two strings s and t of the same length and an integer maxCost.
# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

def equal_substring(s, t, maxCost):
    left, substr_len, abs_val = 0, 0, 0
    for right in range(len(s)):
        abs_val += abs(ord(s[right]) - ord(t[right]))
        while abs_val > maxCost:
            abs_val -= abs(ord(s[left]) - ord(t[left]))
            left += 1
        substr_len = max(substr_len, right - left + 1)
    return substr_len

s = "abcd"
t = "bcdf"
maxCost = 3
print(equal_substring(s, t, maxCost))
print("============")

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

def highest_altitude(gain):
    if len(gain) > 0:
        prefix_sum = [0]
        for i in range(len(gain)):
            prefix_sum.append(gain[i] + prefix_sum[len(prefix_sum) - 1])
    
    return max(prefix_sum)

gain = [-5, 1, 5, 0, -7]
print(highest_altitude(gain))
print("============")

# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

def pivot_index(nums):
    if len(nums) > 0:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[len(prefix_sum) - 1])

        for i in range(len(nums)):
            left = prefix_sum[i] - nums[i]
            right = prefix_sum[len(prefix_sum) - 1] - prefix_sum[i]
            if left == right:
                return i
        
    return -1

nums = [1, 7, 3, 6, 5, 6]
print(pivot_index(nums))
print("============")

# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum_arr = self.create_prefix_sum_arr()

    def sum_range(self, left, right):
        return self.prefix_sum_arr[right] - self.prefix_sum_arr[left] + self.nums[left]

    def create_prefix_sum_arr(self):
        prefix_sum_arr = []
        if len(self.nums) > 0:
            prefix_sum_arr.append(self.nums[0])
            for i in range(1, len(self.nums)):
                prefix_sum_arr.append(self.nums[i] + prefix_sum_arr[len(prefix_sum_arr) - 1])
        return prefix_sum_arr

num_array = NumArray([-2, 0, 3, -5, 2, -1])
print(num_array.sum_range(0, 2))
print(num_array.sum_range(2, 5))
print(num_array.sum_range(0, 5))
print("============")