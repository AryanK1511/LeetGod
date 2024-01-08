# Create Prefix Sum Array
def create_prefix_sum_array(nums):
    if len(nums) > 0:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[len(prefix) - 1])
        return prefix
    return None

nums = [5, 2, 1, 6, 3, 8]
print(create_prefix_sum_array(nums))
print("==============")

# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

def return_bool_arr(nums, queries, limit):
    ans = []
    if len(nums) > 0:
        prefix_sum_arr = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum_arr.append(nums[i] + prefix_sum_arr[len(prefix_sum_arr) - 1])
        
        for i, j in queries:
            prefix_sum = prefix_sum_arr[j] - prefix_sum_arr[i] + nums[i]
            if prefix_sum < limit:
                ans.append(True)
            else:
                ans.append(False)
    return ans


nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

print(return_bool_arr(nums, queries, limit))
print("==============")

# Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.

def number_of_valid_splits(nums):
    count = 0
    if len(nums) > 0:
        prefix_sum_arr = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum_arr.append(nums[i] + prefix_sum_arr[len(prefix_sum_arr) - 1])
    
        for i in range(len(nums) - 1):
            left = prefix_sum_arr[i]
            right = prefix_sum_arr[-1] - prefix_sum_arr[i]
            if left >= right:
                count += 1

        return count
    
def number_of_valid_splits_2(nums):
    total = sum(nums)
    left, count = 0, 0

    for i in range(len(nums) - 1):
        left += nums[i]
        right = total - left
        if left >= right:
            count += 1

    return count

nums = [10,4,-8,7]
print(number_of_valid_splits(nums))
print(number_of_valid_splits_2(nums))
print("==============")

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def running_sum(nums):
    if len(nums) > 0:
        running_sum_arr = [nums[0]]
        for i in range(1, len(nums)):
            running_sum_arr.append(nums[i] + running_sum_arr[len(running_sum_arr) - 1])
        return running_sum_arr
    return None

nums = [1,2,3,4]
print(running_sum(nums))
print("==============")

# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

def minimum_positive_value(nums):
    # if len(nums) > 0:
    #     prefix_sum = [nums[0]]
    #     for i in range(1, len(nums)):
    #         prefix_sum.append(nums[i] + prefix_sum[i - 1])
        
    #     val, res = 0, 0
    #     while res < 1:
    #         val += 1
    #         res = val + min(prefix_sum)
    #     return val
    min_val = 0
    total = 0

    for num in nums:
        total += num
        min_val = min(min_val, total)
    return -min_val + 1

nums = [-3,2,-3,4,2]
print(minimum_positive_value(nums))
print("==============")

# You are given a 0-indexed array nums of n integers, and an integer k.
# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

def k_radius_avg(nums, k):
    avg_arr = [-1 for i in range(len(nums))]
    # Create a prefix sum array
    if len(nums) > 0:
        prefix_sum_arr = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum_arr.append(nums[i] + prefix_sum_arr[len(prefix_sum_arr) - 1])

        total_elements = (k * 2) + 1
        for i in range(k, len(nums) - k):
            total = prefix_sum_arr[i + k] - prefix_sum_arr[i - k] + nums[i - k]
            avg = total // total_elements
            avg_arr[i] = avg
    
    return avg_arr


nums = [7,4,3,9,1,8,5,2,6]
k = 3
print(k_radius_avg(nums, k))