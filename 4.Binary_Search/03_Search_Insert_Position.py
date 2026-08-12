"""
Problem:
Search Insert Position

Pattern:
Binary Search

Difficulty:
Easy

--------------------------------------------------

My First Thought:
As from our discussion - we will use binary search to find the appropriate insert position that
satisfies the predicate P(i): nums[i] >= target

--------------------------------------------------

Observation:
The left pointer after the termination will always point to the index that satisfies the 
predicate and if nums[mid] is equal to the value return the mid index.Invariant : Everything 
before the predicate index is strictly less than the target, everything prom predicate index 
onwards are greater than or equal to the target.

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(log n) , Binary search will take log n time until the loop terminater traversing the list

Space Complexity:
O(1), only for variale declaration

--------------------------------------------------

Learnings:
How binary search can help to find boundary regions apart from finding individual elements in 
a sorted list

Mistakes:

"""

def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1

    return left

nums = [1,3,5,6]
target = 2

print(search_insert(nums, target))