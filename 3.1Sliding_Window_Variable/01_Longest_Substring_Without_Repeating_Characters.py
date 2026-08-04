"""
Problem:
Longest Substring without Repeating Characters

Pattern:
Sliding Window Variable

Difficulty:
Medium

--------------------------------------------------

My First Thought:

How do I maintain a dynamic window and also at the same time continue iterating in the loop. I initially though of moving the pointers, but I couldn't
formulate it. So a Python Set is an ideal choice to be a dynamic window, as it will grow and shrink in O(1) time based on the constraints.
--------------------------------------------------

Observation:
We can use two pointer - left and right. The right pointer will be the optimistic one, and check for evry value in the list and likewise the window
will grow, until a value is found that already exists in the window. Now since the constraint is violated we have to shrik - we increment the left
pointer in the list and remove element from the window(set) until the repeating element is found and removed. Once the constraint is satisfied we 
grow again and return the lenght of the longest substring without repeating characters.

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:


Space Complexity:


--------------------------------------------------

Learnings:
New pattern - Sliding Window

Mistakes:

"""