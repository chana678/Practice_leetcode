"""
Problem:
Squares of Sorted Array

Pattern:
Two Pointer (Converging)

Difficulty:
Easy

--------------------------------------------------

My First Thought:
After squaring the elements of the array, the largest numbers will be on either side of the array.
So I was thinking can I do inplace swap of largest number to the right side with the smallest
number on the right side, but this will take more time and my though is not so clean

--------------------------------------------------

Observation:
After looking up some hint, taking a seperate list and storing it from largest to smallest
and reversing the list will do the job

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(n) for traversing the entire elements in the array

Space Complexity:
O(n), extra space is required for the new list where the elements will be sorted

--------------------------------------------------

Learnings:
Even it is a two pointer approach taking help of an another list to get the answer is right way

Mistakes:
Overthinking, trying to do inplace but taking help of an another list is a good way to solve the
problem. Also has to keep the condition left <= right to take care of that middle value if the 
array length is odd
"""

def sortedSquares(nums):
    squares = [x**2 for x in nums]
    left = 0
    right = len(squares)-1
    sorted_output = []
    while left <= right:
        if squares[left] >= squares[right]:
            sorted_output.append(squares[left])
            left += 1
        
        else:
            sorted_output.append(squares[right])
            right -= 1
    
    return sorted_output[::-1]

nums = [-4,-1,0,3,10]

print(sortedSquares(nums))