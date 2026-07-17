"""
Problem:
Remove Elements

Pattern:
Two Pointer (Parallel)

Difficulty:
Easy

--------------------------------------------------

My First Thought:
Start with two pointers reader and writer on the starting index of the array. Move reader 
from start to the end of the array. The reader will check for the element that is to be removed.
If the element to be removed is found by the reader, the reader will skip ahead to the next 
value that is not to be removed. Now the writer will update its current location with 
that value.

--------------------------------------------------

Observation:
Writer only moves when the element to be removed is repalced .

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
Reader explores and writer replaces the element to be removed with the element that is not
to be removed. Used the continue keyword here to jump ahead

Mistakes:
None, understood the explanation nicely
"""

def removeElement(nums, val):
    writer = 0

    for reader in range(len(nums)):
        if nums[reader] == val:
            continue

        nums[writer] = nums[reader]
        writer += 1

    print(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2

removeElement(nums, val)