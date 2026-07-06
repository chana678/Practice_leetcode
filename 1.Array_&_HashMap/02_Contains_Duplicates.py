"""
Problem:
Contains Duplicates

Pattern:
Hash Set

Difficulty:
Easy

--------------------------------------------------

My First Thought:
Brute force by checking each number with every other number until a duplicate is found. Requires 
two for loop in a nexted form, but since I'm doing this pattern the thought also came to me 
that I can do it in a sincle pass by doing O(1) lookup and insert using a python set. 

--------------------------------------------------

Observation:
I need to know whether I've already seen the number.

--------------------------------------------------

Data Structure Chosen:
Set

Reason:
Allows O(1) lookup of previously seen numbers.

--------------------------------------------------

Time Complexity:
O(n) because I might have to do a whole pass of the array if no solution is found and O(1) 
average lookup and inset for python set. 

Space Complexity:
O(n) because if all the numbers are unique in the list than the python set will take O(n) 
space complexity

--------------------------------------------------

Learnings:
Check the current number in the set. If it already exists return Ture
Otherwise store the number in the set

Mistakes:
None, was able to do it in first try
"""

def containsDuplicates(nums):
    found = set()
    for num in nums:
        if num in found:
            return True
        found.add(num)
    return False

nums = [1,2,3,1]

print(containsDuplicates(nums))
