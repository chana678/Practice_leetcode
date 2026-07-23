"""
Problem:
Sort Colors

Pattern:
Two Pointer (Counting + Construction)

Difficulty:
Medium

--------------------------------------------------

My First Thought:
Elements in the array will only be 0 (red), 1 (white), 2 (blue) colors, so my first though was 
to figure out how many of each colors exists in the array. We will store the count as low,mid 
and high. Now we will start another for loop and if that region exists we will fill that region
if low exist with 0, then mid region with 1 and high region with 2. 

--------------------------------------------------

Observation:
Figuring out the regions if they exists is the key here.

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
This is little bit different from the previous problems, here we are tracking regions and filling
the array appropriately

Mistakes:
None, some hit and trail with the loops (took some time)
"""

def sortColors(nums):
    low, mid, high = 0, 0, 0
    for num in nums:
        if num == 0:
            low += 1
        elif num == 1:
            mid += 1
        else:
            high += 1

    for reader in range(len(nums)):
        if reader < low:
            nums[reader] = 0
        elif low <= reader < low + mid:
            nums[reader] = 1
        else:
            nums[reader] = 2

nums = [2,0,2,1,1,0]

sortColors(nums)
