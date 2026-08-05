"""
Problem:
Minimum Size Subarray Sum

Pattern:
Sliding Window Variable

Difficulty:
Medium

--------------------------------------------------

My First Thought:
If I could find the first window that satisfy the constraint , then other window that satify the
constraint will have length less than or equal to that first window. Now I straigh away though of
jumping the left and right pointer to the next of right pointer if a window that satisfy the
constraint is found. But I was wrong, So I had to look up examples online and took some hint 
on why even within the larger window there could be solution with smaller window that satisfy 
the constraint. Also we don't have to find the initial sum as we though of outside the loop,
the continious sum will take care of it. 

--------------------------------------------------

Observation:
Same as my first thought.

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(n), There is a nested loop but the inner loop will visit the elements of the list atmost once,
because the left pointer is not moving backwards.


Space Complexity:
O(1) , for variable declaration 

--------------------------------------------------

Learnings:
New ways of solving problem

Mistakes:

"""

def minSubArrayLen(target,nums):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum = current_sum - nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

target = 10
nums = [1, 1, 1, 10, 20, 1]

print(minSubArrayLen(target,nums))