"""
Problem:
Longest Repeating Character Replacement

Pattern:
Sliding Window Variable

Difficulty:
Medium

--------------------------------------------------

My First Thought:
We have to maintain a window of repeating characters where the replacement that can be done
is atmost k.
--------------------------------------------------

Observation:
After some (more) help from hints - We have to maintain a frequency hash map for characters . The right
pointer will move along and we will calculate window size. Now we will also calculate replacement
= window length - max frequency. What this replacement is telling us that if it is greater than k
then our current window is violating the constraint. So we will decrement the charater frequency
pointed by left. At the end we will return the window length. The window length at the end may 
contain garbage values, but because of the max_frequency that we took and the replacement
condition the window size gets locked at the maximum valid window length. The window size
can only grow if it finds a frequency greater than the current max frequency, at that time the 
replacement >k condition will evaluate to false and the left pointer will not be incremented. 

--------------------------------------------------

Data Structure Chosen:
Dictionary

Reason:
To store the frequency of the characters

--------------------------------------------------

Time Complexity:
O(n), to do one pass of the string


Space Complexity:
O(1), as the string contain only capital english characters wich is of size 26 and the values are 
the frequency count of the characters.

--------------------------------------------------

Learnings:
New pattern - Sliding Window - Variable with Max Frequency

Mistakes:

"""