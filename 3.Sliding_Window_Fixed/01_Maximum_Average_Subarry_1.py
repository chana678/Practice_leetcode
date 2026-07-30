"""
Problem:
Maximum Average Subarray 1

Pattern:
Sliding Window Fixed

Difficulty:
Easy

--------------------------------------------------

My First Thought:
We will start with two pointers left(starting index) and right(value of k). This region will
form a window. We wil compute the sum ,compute the average and move the window by one position 
to the right meaning both left and right index will move one position. We visit all the 
windows possible and return the maximum average. 

--------------------------------------------------

Observation:
Same as my first though. When I write down how the invariant is working, I'm able to visualize 
the window is moving. Sure coding is there some erros, if and buts here and there will happen
but understanding the logic is fun.

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
O(n) , we are going to do a one pass over the entire list to get the maximum average for a window,
also we have to calculate the sum for each window, so that will take k (finite) amount of time.

Space Complexity:
O(1), only for variale declaration

--------------------------------------------------

Learnings:
New pattern - Sliding Window

Mistakes:
I was making the beginner mistake, despite learning the logic, I was computing the sum for all
the indivisual windows, then when time out occured for few of the test cases, I realized I was 
wrong, after that I implemented it correctly.
"""

def findMaxAverage(nums, k):
    left = 0
    right = k
    current_sum = sum(nums[left:right])
    max_avg = current_sum / k

    while right < len(nums):
        present_sum = current_sum - nums[left] + nums[right]
        print(present_sum)
        right += 1
        left += 1
        present_avg = present_sum / k
        current_sum = present_sum

        if present_avg > max_avg:
            max_avg = present_avg

    return max_avg


    

nums = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(nums, k))
