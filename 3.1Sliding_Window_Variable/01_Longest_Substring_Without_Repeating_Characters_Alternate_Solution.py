'''
Alternate Solution using HashMap

'''

def lengthofLongestSubstring(s):
    last_seen = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]

        if char in last_seen and last_seen[char] >= left:
            left = max(left, last_seen[char] + 1)
            
        last_seen[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length

s = "pwwkew"
print(lengthofLongestSubstring(s))