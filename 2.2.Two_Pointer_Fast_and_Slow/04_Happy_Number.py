"""
Problem:
Happy Number

Pattern:
Two Pointer (Fast and Slow)

Difficulty:
Easy

--------------------------------------------------

My First Thought:
One way I thought of doing this one was keep on finding the sum and storing it in a set.
If we encounter 1 we can return true, otherwise continue to sum and if a sum already exists
in the set then return False, like finding a cycle.

--------------------------------------------------

Observation:
So you told me we can use Floyds Algorithm to solve this problem. I had to look up some hints to 
solve this using Floyds Algorithm but I got the idea, mostly the hints helped a lot here. We will
use a helper function here to calculate the sum. We will use two variables here slow and fast,
initially slow and fast both will hold the initial number, then inside the while loop slow will
find the immediate next sum and fast will find the next to next sum. If fast is 1 we return True 
otherwise if fast and slow meet meaning a cycle exists and fast is not equal to 1 then we return 
False.

--------------------------------------------------

Data Structure Chosen:
None

Reason:
None

--------------------------------------------------

Time Complexity:
For the time complexity part I have some doubt. most of the work is going to be finding the sum of
numbers . So I looked up online and found out that a number n can have maximum log(base 10)n + 1 
digits. And even for the largest 2^32 bit integer the sum comes out to be a small number which is 
going to be a finite set of numbers hence each step in the while loop whill take constant time.
So total time complexity will be O(log n). But please explain to me in details about the time
complexity here.

Space Complexity:
O(1) for variable declaration

--------------------------------------------------

Learnings:
Floyds Algorithm is useful even when there is no linked list. We just have to look long enough to 
find the pattern that detecting cycle can be in other areas also where linked list is not used.

Mistakes:
None, Floyds Algorithm helped a lot
"""

def getSum(num):
    sum_square = sum([int(n)**2 for n in str(num)])
    return sum_square

def isHappy(num):
    slow = num
    fast = num

    while fast:
        slow = getSum(slow)
        fast = getSum(getSum(fast))

        if fast == 1:
            return True

        if slow == fast and fast != 1:
            return False

print(isHappy(19))