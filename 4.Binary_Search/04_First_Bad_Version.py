"""
Problem:
First Bad Version

Pattern:
Binary Search

Difficulty:
Easy

--------------------------------------------------

My First Thought:
As from our discussion - we will use binary search to fnd the first bad version.

--------------------------------------------------

Observation:
Here the API is already defined, The invariant is if a bad version exists - it exists between
the range [left,right], the boundary shrinks when left == right.

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(log n) , Binary search will take log n time until the loop terminater.

Space Complexity:
O(1), only for variale declaration

--------------------------------------------------

Learnings:
Using Binary Search to find the boundary for a different type of problem.

Mistakes:

"""

# Simulating Bad version API
def bad_version(val):
    '''
    Simulating the bad version api
    '''
    bad_set = {7,8,9,10}

    return True if val in bad_set else False

def first_bad_version(n):
    '''
    Function to find the first bad version
    '''
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2

        if bad_version(mid):
            right = mid

        else:
            left = mid + 1

    return left

print(first_bad_version(10))