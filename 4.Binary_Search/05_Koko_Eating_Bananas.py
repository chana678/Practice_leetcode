"""
Problem:
Koko Eating Bananas

Pattern:
Binary Search

Difficulty:
Medium

--------------------------------------------------

My First Thought:
As from our discussion - This is a type of finding first bad version problem

--------------------------------------------------

Observation:
The invariant is finding the minimum hours to finish eating the bananas and it lies in the 
region [left,right], where left = 1 and right = max(piles)

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(nlog m) , Binary search will take log m (were m is the range of speed values) time until the 
loop terminater and for every mid value in the speed range we will calculate the time taken to 
eat the bananas in hours . Each calculation is equal to the length of the list of length n. 

Space Complexity:
O(1), only for variale declaration

--------------------------------------------------

Learnings:
This is a kind of first bad version problem.

Mistakes:

"""

def min_eating_speed(piles, h):
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        hours = 0

        for num in piles:
            hours += (num + mid - 1) // 2 

        if hours <= h:
            right = mid
        else:
            left = mid + 1

    return right

piles = [30,11,23,4,20]
h = 5

print(min_eating_speed(piles, h))