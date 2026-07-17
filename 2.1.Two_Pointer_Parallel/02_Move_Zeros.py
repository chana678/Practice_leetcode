"""
Problem:
Move Zeros

Pattern:
Two Pointer (Parallel)

Difficulty:
Easy

--------------------------------------------------

My First Thought:
Start with two pointers reader and writer on the starting index of the array. Move reader 
from start to the end of the array. The reader will check for non-zero values and copy the
non-zero value to the writer location preserving the order in which they originally appear

--------------------------------------------------

Observation:
Writer only moves when a non-zero value is encountered by the reader

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
Reader explores and writer commits the non zero value in the original order

Mistakes:
None, understood the explanation nicely
"""

def moveZeros(nums):
    writer = 0

    for reader in range(len(nums)):
        if nums[reader]:
            nums[writer] = nums[reader]
            writer += 1

    for i in range(writer,len(nums)):
        nums[i] = 0
    
    print(nums)

nums = [0,1,0,3,12]

moveZeros(nums)