# Palindrome String
def is_palindrome(s):
    # Create two pointers from left and right
    left = 0
    right = len(s) - 1

    # Loop until the pointers either meet or right before left > right
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1 # Increment Left
        right -= 1 # Decrement Right

    return True

print(is_palindrome("racecar"))
print(is_palindrome("abcb"))
print("++++++++++++++++++++")

# Two sum with sorted list
def sorted_two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        # If curr is greater than the target than we have to make the number smaller
        if curr > target:
            right -= 1
        # Vice versa
        else:
            left += 1
    
    return False
                

nums = [1, 2, 4, 6, 7, 8, 14, 15]
target = 11
print(sorted_two_sum(nums, target))
print("++++++++++++++++++++")