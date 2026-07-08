"""
Problem:
Valid Anagram

Pattern:
Hash Map

Difficulty:
Easy

--------------------------------------------------

My First Thought:
Can I do it in a single pass, It took me really some time to figure out how to do it, 
I thought if the characters were not repeating then we can use a hash set and do a pop operation 
every time the character is encountered in the right string and at the end chek if the set is 
empty, but since the characters are repeating we have to use a hash map and do some from of 
increment and decrement operation on the dictionary values while maintaing all this happens in a 
single pass

--------------------------------------------------

Observation:
I need to increment value in the dict for character in left string, and decrement value in the 
dict for character in the right string

--------------------------------------------------

Data Structure Chosen:
Dictionary

Reason:
Allows O(1) lookup of keys and O(1) time for addition/substraction of values.

--------------------------------------------------

Time Complexity:
O(n) because checking for anagram will required traversing the array till end and O(1) time for
dictionary lookuo and operation on values 

Space Complexity:
O(n) beacuse if all the characters are unique , dictionary will require n space for key value pair.

--------------------------------------------------

Learnings:
The problem was not that difficult but my overthinking made it complex. Small steps
and practice is important. Sometimes simple dictionary manipulation does the job

Mistakes:
Non as such but it shouldn't take me so much time to figure out the solution
"""

from collections import defaultdict

def isAnagram(s,t):
    frequency = defaultdict(int)

    if len(s) != len(t):
        return False

    for left,right in zip(s,t):
        frequency[left] += 1
        frequency[right] -= 1

    return True if not any(frequency.values()) else False

s = "rat" 
t = "car"

print(isAnagram(s,t))