"""
Problem:
Fruit into Basket

Pattern:
Sliding Window Variable

Difficulty:
Medium

--------------------------------------------------

My First Thought:
Honestly for this problem I was blank on how to approach it. When you told me we can use a Hashmap 
I was confused on how do I perform a varible sliding window with hashmap elimination. I have to 
seriously lookup some hints on how hashmap elimination is related to the problem.
--------------------------------------------------

Observation:
Invariant: The problem description is long but the core idea is to find the length of the longest
sub array that can contain atmost two distinct elements. Now thanks to the hints our dictionary
will act as the window.

--------------------------------------------------

Data Structure Chosen:
Dictionary

Reason:
To store the count of elements and use it as a sliding window

--------------------------------------------------

Time Complexity:
O(n), There is a nested loop, but the inner loop will only visit a element atmost once. Left
pointer will not decrement.


Space Complexity:
O(n) , for the dictionary, n because if the length of the list is n and all the values in 
the list are unique then we will require n (key,value) pair.

--------------------------------------------------

Learnings:
New pattern - Sliding Window - Variable along with HasHMap elimination

Mistakes:

"""
from collections import defaultdict

def totalFruit(fruits):
    seen = defaultdict(int)
    left = 0
    max_lenght = 0

    for right in range(len(fruits)):
        seen[fruits[right]] += 1

        while len(seen) > 2:
            seen[fruits[left]] -= 1

            if seen[fruits[left]] == 0:
                seen.pop(fruits[left])
            left += 1

        max_lenght = max(max_lenght, right - left + 1)

    return max_lenght

fruits = [1,2,3,2,2]

print(totalFruit(fruits))