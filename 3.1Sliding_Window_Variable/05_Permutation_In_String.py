"""
Problem:
Longest Repeating Character Replacement

Pattern:
Sliding Window Variable

Difficulty:
Medium

--------------------------------------------------

My First Thought:
The permutation of string s1 can be converted into a frequency map.
--------------------------------------------------

Observation:
We have to maintain a window of lenght == length of s1 and the character frequency of the 
window should maintain the charater frequency of string s1. 

--------------------------------------------------

Data Structure Chosen:
Dictionary

Reason:
To store the frequency of the characters

--------------------------------------------------

Time Complexity:
O(n), to do one pass of the string


Space Complexity:
O(1), as the string contain only lowercase english characters wich is of size 26 and the values are 
the frequency count of the characters.

--------------------------------------------------

Learnings:
New pattern - Sliding Window - Variable new Invariant - Permutation in String

Mistakes:

"""

def checkInclusion(s1, s2):
    core_freq = {}
    for char in s1:
        core_freq[char] = 1 + core_freq.get(char, 0)

    left = 0
    window = {}

    for right in range(len(s2)):
        window[s2[right]] = 1 + window.get(s2[right], 0)

        if right - left + 1 == len(s1):
            if window == core_freq:
                return True

            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                window.pop(s2[left])
            left += 1

    return False

s1="adc"
s2="dcda"

print(checkInclusion(s1,s2))
             