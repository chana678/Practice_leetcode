"""
Problem:
Container with most water

Pattern:
Two Pointer (Converging)

Difficulty:
Medium

--------------------------------------------------

My First Thought:
Start with pointers on either ends of the array, calculate area then move the pointer who height
is less of the two.

--------------------------------------------------

Observation:
Lower height determines the height of the container

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(n) for traversing the entire heights in the array

Space Complexity:
O(1) for variable declaration

--------------------------------------------------

Learnings:
From your explanation if heights are equal then incrementing the left pointer and decrementing
the left pointer at the same time is good.

Mistakes:
None, figured out the problem but you polished it.
"""

def maxArea(height):
    left = 0
    right = len(height)-1
    max_area = 0
    while left < right:
        width = right - left
        area = width * min(height[left], height[right])
        max_area = max(max_area,area)
        
        if height[left] == height[right]:
            left += 1
            right -= 1
        
        elif height[left] < height[right]:
            left += 1

        else:
            right -= 1
    
    return max_area

height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))