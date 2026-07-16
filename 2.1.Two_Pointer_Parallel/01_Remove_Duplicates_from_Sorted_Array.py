"""
Problem:
Remove Duplicates from Sorted Aray

Pattern:
Two Pointer (Parallel)

Difficulty:
Easy

--------------------------------------------------

My First Thought:
Start with two pointers reader and writer on the starting index of the array. Move reader 
from start to the end of the array. Move writer one step only if the reader has encountered
a new value. Update that location with the new value from reader

--------------------------------------------------

Observation:
Writer only moves when a new value is encountered by reader. Everything before the writer is 
already in deduplicated form

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(n) for reading the entire array once by reader 

Space Complexity:
O(1) for variable declaration

--------------------------------------------------

Learnings:
Reader explores and writer commits

Mistakes:
None, understood the explanation nicely
"""