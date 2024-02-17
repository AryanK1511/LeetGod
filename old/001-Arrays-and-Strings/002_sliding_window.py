# Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.
def longest_subarray(nums, k):
    # Using sliding window
    curr, ans, left = 0, 0, 0

    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)

    return ans
        

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
print(longest_subarray(nums, 8))
print("===============")

# Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

def longest_binary_substring(s):
    left, num_zeroes, ans = 0, 0, 0

    for right in range(len(s)):
        if s[right] == "0":
            num_zeroes += 1
        while num_zeroes > 1:
            if s[left] == "0":
                num_zeroes -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans


s = "1101100111"
print(longest_binary_substring(s))
print("===============")

# Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.
# For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

def max_valid_subarrays(nums, k):
    left, product, number_of_subarrays = 0, 1, 0
    
    if k <= 1:
        return 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product /= nums[left]
            left += 1

        number_of_subarrays += (right - left + 1)
    return number_of_subarrays

nums = [10, 5, 2, 6]
k = 3

print(max_valid_subarrays(nums, k))
print("===============")

# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

def find_subarr_with_largest_sum(nums, k):
    sum = 0
    for i in range(k):
        sum += nums[i]
    
    max_sum = sum
    for i in range(k, len(nums)):
        sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, sum)
    
    return max_sum


nums = [3, -1, 4, 12, -8, 5, 6]
k = 4
print(find_subarr_with_largest_sum(nums, k))
print("===============")

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

def find_max_average(nums, k):
    left, avg, max_avg, sum = 0, 0, 0, 0

    for right in range(k):
        sum += nums[right]

    avg = sum / k
    max_avg = avg

    for right in range(k, len(nums)):
        sum += nums[right] - nums[left]
        avg = sum / k
        left += 1
        right += 1
        max_avg = max(max_avg, avg)

    return max_avg

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(find_max_average(nums, k))
print("===============")

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

def max_consecutive_ones(nums, k):
    left, max_window_size, num_zeroes = 0, 0, 0

    for right in range(len(nums)):
        if nums[right] == 0:
            num_zeroes += 1
        while num_zeroes > k:
            if nums[left] == 0:
                num_zeroes -= 1
            left += 1

        max_window_size = max(max_window_size, right - left + 1)

    return max_window_size

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(max_consecutive_ones(nums, k))
print("===============")