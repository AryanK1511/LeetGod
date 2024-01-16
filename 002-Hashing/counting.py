# You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
def func(s, k): 
    d = {}
    left, ans = 0, 0

    for right in range(len(s)):
        if s[right] not in d:
            d[s[right]] = 1
        else:
            d[s[right]] += 1
        while len(d) > k:
            if d[s[left]] == 1:
                del d[s[left]]
            else:
                d[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans

s = "eceba"
k = 2

print(func(s, k))
print("============")

# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
def array_intersection(nums):
    d = {}
    arr = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] not in d:
                d[nums[i][j]] = 1
            else:
                d[nums[i][j]] += 1

    for element in d:
        if d[element] == len(nums):
            arr.append(element)

    return sorted(arr)

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(array_intersection(nums))
print("============")

# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
def are_occurrences_equal(s):
    occurrences = {}
    for char in s:
        if char not in occurrences:
            occurrences[char] = 1
        else:
            occurrences[char] += 1
    
    return len(set(occurrences.values())) == 1

s = "abacbc"
print(are_occurrences_equal(s))
print("============")

# Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
def subarray_count(nums, k):
    counts = {0: 1}
    sum, total = 0, 0

    for right in range(len(nums)):
        sum += nums[right]
        if sum - k in counts:
            total += counts[sum - k]

        if sum not in counts:
            counts[sum] = 1
        else:
            counts[sum] += 1
        
    return total

nums = [1, -1, 0]
k = 0
print(subarray_count(nums, k))
print("============")

# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

def num_subarr(nums, k):
    counts = {0: 1}
    sum, total = 0, 0

    for right in range(len(nums)):
        sum += nums[right] % 2
        if sum - k in counts:
            total += counts[sum - k]

        if sum not in counts:
            counts[sum] = 1
        else:
            counts[sum] += 1
        
    return total

nums = [1, 1, 2, 1, 1]
k = 3
print(num_subarr(nums, k))
print("============")

# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
#Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
def find_players(matches):
    match_data = {}
    for match in matches:
        if match[0] not in match_data:
            match_data[match[0]] = 0
        if match[1] not in match_data:
            match_data[match[1]] = 0 
        
        match_data[match[1]] += 1

    return [sorted([player for player in match_data if match_data[player] == 0]), sorted([player for player in match_data if match_data[player] == 1])]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(find_players(matches))
print("============")

# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
def return_largest_number(nums):
    num_counter = {}
    for num in nums:
        if num not in num_counter:
            num_counter[num] = 1
        else:
            num_counter[num] += 1
    ans = [number for number in num_counter if num_counter[number] == 1]
    return max(ans) if len(ans) > 0 else -1

nums = [5,7,3,9,4,9,8,3,1]
print(return_largest_number(nums))
print("============")

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
def max_balloons(text):
    return min(text.count('b'), text.count('a'), text.count('l') // 2, text.count('o') // 2, text.count('n'))

text = "loonbalxballpoon"
print(max_balloons(text))
print("============")

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
def find_max_length(nums):
    count_map = {0: -1}
    max_len = count = 0
    index = 0

    for num in nums:
        count += 1 if num == 1 else -1

        if count in count_map:
            max_len = max(max_len, index - count_map[count])
        else:
            count_map[count] = index

        index += 1

    return max_len

nums = [0, 1, 1]
print(find_max_length(nums))
print("============")