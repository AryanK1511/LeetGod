# Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

def two_sum(nums, target):
    d = {}
    for i in range(len(nums)):
        if (target - nums[i]) in d:
            return [d[target - nums[i]], i]
        d[nums[i]] = i
    return None

nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))
print("============")

# Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.

def repeated_character_slow(s):
    char_count = {}
    for i in range(len(s)):
        if s[i] not in char_count:
            char_count[s[i]] = 1
        else:
            char_count[s[i]] += 1

        if char_count[s[i]] >= 2:
            return s[i]
    return None

def repeated_character(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return char
        char_set.add(char)
    return None

s = "abccbaacz"
print(repeated_character(s))
print("============")

# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

def check_if_pangram(sentence):
    seen_words = set(sentence)
    return len(seen_words) == 26

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(check_if_pangram(sentence))
print("============")

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missing_number(nums):
    nums_set = set(nums)
    n = len(nums) + 1
    for i in range(n):
        if i not in nums_set:
            return i

nums = [3, 0, 1]
print(missing_number(nums))
print("============")

# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

def count_elements(arr):
    arr_set = set(arr)
    count = 0
    for x in arr:
        if x + 1 in arr_set:
            count += 1
    return count

arr = [1, 2, 3]
print(count_elements(arr))
print("============")
