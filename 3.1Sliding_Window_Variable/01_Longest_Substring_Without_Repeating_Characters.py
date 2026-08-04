"""
Problem:
Longest Substring without Repeating Characters

Pattern:
Sliding Window Variable

Difficulty:
Medium

--------------------------------------------------

My First Thought:

How do I maintain a dynamic window and also at the same time continue iterating in the loop. I 
initially though of moving the pointers, but I couldn't formulate it. So a Python Set is an 
ideal choice to be a dynamic window, as it will grow and shrink in O(1) time based on the 
constraints.
--------------------------------------------------

Observation:
We can use two pointer - left and right. The right pointer will be the optimistic one, and check 
for every value in the list and likewise the window will grow, until a value is found that already 
exists in the window. Now since the constraint is violated we have to shrik - we increment the left
pointer in the list and remove element from the window(set) until the repeating element is found 
and removed. Once the constraint is satisfied we grow again and return the lenght of the longest 
substring without repeating characters.

--------------------------------------------------

Data Structure Chosen:
Set

Reason:
Removing an element and Inserting an element takes O(1) time

--------------------------------------------------

Time Complexity:
O(n), There is a nested loop, but for every element in the outer loop, we are not visiting every
element in the inner for loop. Only when the constraint is violated we visit the inner loop, and 
even if we have to visit the inner for loop again we will not visit the part of array that was 
already visited by the inner loop in it's previous iteration. So a factor of k which is a 
finite number is added to the time complexity. And in time complexity higher terms are considered,
hence time complexity is O(n)


Space Complexity:
O(n) , as we will need storage for the window, n because if the length of the longest substring
without repeating characters is equal to n

--------------------------------------------------

Learnings:
New pattern - Sliding Window - Variable

Mistakes:

"""

def lengthofLongestSubstring(s):
    window = set()
    left = 0
    max_length = 0

    for right in s:
        if right not in window:
            window.add(right)

        else:
            if len(window) > max_length:
                max_length = len(window)

            while right in window:
                window.remove(s[left])
                left += 1
            window.add(right)

    if len(window) > max_length:
        max_length = len(window)

    return max_length

s = "pwwkew"
print(lengthofLongestSubstring(s))