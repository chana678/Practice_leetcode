"""
Problem:
Maximum Number of vowels in a substring of given length k

Pattern:
Sliding Window Fixed

Difficulty:
Medium

--------------------------------------------------

My First Thought:
We will start with two pointers left(starting index) and right(value of k). This region will
form a window. We will store the vowels in a set for quick lookup. For the first window we will
caluclate the number of vowels outside the loop, now from the second loop onwards if the outgoing
left element is a vowel we will subtract from the previous window vowel count and if the incoming 
element is a vowel we will add to the current window vowel count. Finally we will return the 
maximum number of vowel count in a substring of length k.

--------------------------------------------------

Observation:
We are using hash set so I am starting to see some pattern overlap on how one pattern can 
assist the other.

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(n) , we are going to do a one pass over the entire string, and a small finite time k to traverse 
the first window to calculate it's total vowel count.

Space Complexity:
O(k), for a set to store the number of vowels. Since the lenght will be 5 was can safely say
space complexity is O(1)

--------------------------------------------------

Learnings:
New pattern - Sliding Window

Mistakes:

"""

def maxVowels(s,k):
    vowels = {"a","e","i","o","u"}
    left = 0
    right = k
    current_vowels = sum(1 for char in s[left:right] if char in vowels)
    max_vowels = current_vowels

    while right < len(s):
        if s[left] in vowels and s[right] not in vowels:
            present_vowels = current_vowels - 1

        elif s[right] in vowels and s[left] not in vowels:
            present_vowels = current_vowels + 1
        else:
            present_vowels = current_vowels

        current_vowels = present_vowels
        left += 1
        right += 1

        if present_vowels > max_vowels:
            max_vowels = present_vowels

    return max_vowels

s = "abciiidef"
k = 3

print(maxVowels(s,k))