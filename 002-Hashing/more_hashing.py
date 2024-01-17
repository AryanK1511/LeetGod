# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def group_anagrams(strs):
    groups = {}

    for s in strs:
        key = "".join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    return list(groups.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
print("=================")

# You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.
# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

def min_consecutive_cards(cards):
    left, min_window = 0, float('inf')
    counts = {}
    for right in range(len(cards)):
        if cards[right] in counts:
            counts[cards[right]] += 1
        
            while counts[cards[right]] > 1:
                counts[cards[left]] -= 1
                left += 1
            min_window = min(min_window, right - left + 2)
        else:
            counts[cards[right]] = 1

    return min_window if min_window < float('inf') else -1

cards = [3,4,2,3,4,7]
print(min_consecutive_cards(cards))
print("=================")