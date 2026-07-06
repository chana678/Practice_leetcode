"""
Problem:
Two Sum

Pattern:
Hash Map

Difficulty:
Easy

--------------------------------------------------

My First Thought:
Brute force by checking every pair. Taking Two nested for loops and finding the pair that equated to the sum

--------------------------------------------------

Observation:
I need to know whether I've already seen the complement.

--------------------------------------------------

Data Structure Chosen:
Dictionary

Reason:
Allows O(1) lookup of previously seen numbers.

--------------------------------------------------

Time Complexity:
O(n) because in the worst case I might have to traverse to the end of the list to find the compliment

Space Complexity:
O(n) because the dictionary might take up n-1 space to store the compliment and it's index

--------------------------------------------------

Learnings:
Store the current number only after checking for its complement.
Otherwise, the same element could match itself.

Mistakes:
Was storing the compliment as a key in the dictionary instead of the number at index position i, but figured it out.
"""



def twoSum(nums, target):
    dict_comp = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in dict_comp:
            return [dict_comp[compliment],i]
        dict_comp[nums[i]] = i


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))