"""
Problem:
Find the Duplicate Number

Pattern:
Two Pointer (Fast and Slow)

Difficulty:
Medium

--------------------------------------------------

My First Thought:
Couldn't figure out how to deal with this, looked up some hints to see how to move the data 
with respect to floyds algorithm. I didn't paid much attention to the constraints of th problem. 
Now the value in the list will always be a value between 1 and the length of the list. So the 
fast pointer can jump twice using the value of the first jump as an index, and since there is a
duplicate number in the list , we will run the loop until slow is equal to fast.This part proves
that a cycle exists and the second part we will reset fast to inde 0 and keep slow as is and 
move each pointer by one step. And when fast and slow meet that node will be the entry point
of the cycle . We will return the node meaning the value

--------------------------------------------------

Observation:
Need to look more carefully at the problem constraints, also this approach and the previous one - 
happy number is something new - I leaned arrays can also behave as a linked list under right 
conditions but I also took hint as help.

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
Little bit confused about the time complexity but more or less we will traverse the entire list
in form or index pointing to some index before they meet. And after they meet again we have to 
find the cycle entry point . So it will be O(n) , k being the minor factor where we need to 
visit few nodes to find the Cycle Entry Point.

Space Complexity:
O(1) for variable declaration

--------------------------------------------------

Learnings:
Arrays can also be used as a linked list and doing so we can apply floyds algorithm to it to
find the duplicate number.

Mistakes:
None, Floyds Algorithm helped a lot
"""

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

nums = [1,3,4,2,2]
print(findDuplicate(nums))