"""
Problem:
Minimum Window Substring

Pattern:
Sliding Window Variable

Difficulty:
Hard

--------------------------------------------------

My First Thought:
I have to find the characters of string t as a substring in string s. I can use a dictionary
to store the frequency of characters of string t and find the same frequency of characters
as substring in s
--------------------------------------------------

Observation:
Here the string t can contain duplicate characters, and also we are going to store the 
characters of string s in another dictionary. Now we cannot compare dictionary here because the 
character frequency count can differ in dictonary_s until we find our first window. So instead
we can use a counter variable where the counter varibale will only get incremented if the 
character frequecy of that character matches the character frequecy of target dictionay if that 
character is in target dictionary. Now once the counter is equal to the lenght of the target
dictionary we know that we hav found our first window. We will calculate the min_length of the 
window and and store its left and right pointer as best_start and best_end. Now our objective is 
to find the minimum lenght substring, so within the current window we will have to check if
a smaller window exists that satisfies our condition. Now once we calculate the window length
and store its positions, we will decrement the character frequency of the element pointed by 
left pointer in the window and then we will check if the element exists in target dictionary
and whether its current count is less that target dictionsy count. If so then we will decrement
counter value by , an finally we will increment the left pointer by 1. Why we are decrementing
the counter is beacause the current window doesnot have all the right character frequencies 
to be a valid window. 

--------------------------------------------------

Data Structure Chosen:
Dictionary

Reason:
To store the frequency of the characters

--------------------------------------------------

Time Complexity:
O(m + n), where n is the length of the string t and we do a one pass over it to store the 
character frequencies and m is the length of the string s where we do a one pass to 
find our min length window. There is a while loop inside the for loop of s, but the elements 
of string s will only be visited at most once by the while loop so the time complexity
increases by a factor of plus m not a multiple of m.


Space Complexity:
O(1), as the strings can contain only uppercase and lowercase english characters wich is of 
size 52 (finite size) and the values are the frequency count of the characters.

--------------------------------------------------

Learnings:
New pattern - Sliding Window - More or less all the concepts of the previous problems of variable 
sliding window was used in this problem.

Mistakes:
After I decremented the character frequency and checked for condition if a smaller valid window
exist , I was using the != to condition, this was wrong of me, it will only work if we hae ditinct
character, since it contains duplicates the right operator should be < (this one I had to lookup
as a hint.)
"""

def minWindow(s,t):
    target = {}
    for char in t:
        target[char] = 1 + target.get(char,0)
    left = 0
    min_len = float("inf")
    best_start = -1
    best_end = -1
    counter = 0
    window = {}

    for right in range(len(s)):
        ch = s[right]
        window[ch] = 1 + window.get(ch, 0)
        if ch in target and window[ch] == target[ch]:
            counter += 1

        while counter == len(target):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                best_start = left
                best_end = right

            val = s[left]
            window[val] -= 1

            if val in target and window[val] < target[val]:
                counter -= 1

            left += 1

    return s[best_start:best_end+1]

s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s,t))