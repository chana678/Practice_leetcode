"""
Problem:
Valid Palindrome

Pattern:
Two Pointer (Converging)

Difficulty:
Easy

--------------------------------------------------

My First Thought:
Remove non english characters, whitespaces and convert to lowercase

--------------------------------------------------

Observation:
Start with two pointers on either side of the string , starts matching until left pointer equal
to right pointer. Return False if at any point left element not equal to right element otherwise
return True

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(n) , where n = i+j, i being the left pointer and j being the right pointer

Space Complexity:
O(k), where k is the size of the string after removing white spaces, special, non-english 
characters

--------------------------------------------------

Learnings:
I have to lookup regular expression to clean the string

Mistakes:
I was getting confuse in the while condition eventually figured out keeping left < right 
also solve empty string problem rather than me writing another if condition. Also I overlooked
the question and was working only on english characters but the question said alphanumeric
characters. Eventually fixed it
"""

import re

def isPalindrome(s):
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    left = 0
    right = len(cleaned_string)-1
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1
    return True

s = "0P"

print(isPalindrome(s))