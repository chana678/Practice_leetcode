"""
Problem:
Longest Consecutive Sequence

Pattern:
Hash Map

Difficulty:
Medium

--------------------------------------------------

My First Thought:
My first thought was to sort the list, but the solution needs to happen in O(n) time, hence 
sorting is not the solution. 

--------------------------------------------------

Observation:
After taking some hint, we can use a Hash Set to find the root number in a list and start finding
root+1, root+2 numbers and return the length of the longest sequence possible

--------------------------------------------------

Data Structure Chosen:
Set

Reason:
Allows O(1) lookup of elements

--------------------------------------------------

Time Complexity:
O(n + k), n because we will have to do a one pass over the entire list, and k because for a 
particular element if that element is the root element then we will ahev to find the sequence, and
lets say the sequence lenght is equal to the length of the list, then once we find the root 
element, we will traverse the inner for loop for the remaing n-1 elements only once, the while
loop will get omitted for the rest of the elements in the outer for loop. Hence the time 
complexity is O(n) instead of O(n^2)

Space Complexity:

O(n) , to create a set from the list
--------------------------------------------------

Learnings:
I learned that even thought we are using nested for loop , the time complexity doesn't have to be
O(n^2). The conditions define how the inner loop will get executed and hence the time complexity
can be O(n)

Mistakes:
Took some help/hints to solve the problem, was unable to wrap the head until saw some hints.
"""

def longestSequence(nums):
    nums_set = set(nums)
    longest_seq = 0

    for num in nums_set:
        count = 1
        if num-1 not in nums_set:
            current_num = num

            while current_num+1 in nums_set:
                count += 1
                current_num += 1

            if count > longest_seq:
                longest_seq = count

    return longest_seq

nums = [100,4,200,1,3,2]

print(longestSequence(nums))
            
