"""
Problem:
Two Sum II

Pattern:
Two Pointer (Converging)

Difficulty:
Medium

--------------------------------------------------

My First Thought:
Array is sorted, so we can use Two Pointer approach to find the sum and return the indices

--------------------------------------------------

Observation:
Start with two pointers on either side of the array, find sum. IF sum is lower increment 
left pointer otherwise decrement right pointer

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(n) where n being the number of elements in the array

Space Complexity:
O(1), No extra space is required as compared to Two Sum, only two variable declaration is required

--------------------------------------------------

Learnings:
If the array is sorted, Two Sum problem can be solved without any extra spaces using Two
Pointer approach

Mistakes:
None in this one
"""

def twoSum(numbers,target):
    left = 0
    right = len(numbers)-1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left+1,right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

nums = [2,7,11,15] 
target = 9

print(twoSum(nums,target))