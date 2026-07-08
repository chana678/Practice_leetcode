"""
Problem:
Group Anagrams

Pattern:
Hash Map

Difficulty:
Medium

--------------------------------------------------

My First Thought:
Grouping is there so some form of hash map can be used

--------------------------------------------------

Observation:
After taking the hint from you, I need to generate a unique signature for the possible anagrams

--------------------------------------------------

Data Structure Chosen:
Dictionary

Reason:
Allows O(1) lookup of keys

--------------------------------------------------

Time Complexity:
O(n.klogk + t), where n is the number of words in the list and k is the length of each 
word(Timsort), t for the next for loop to append it to the final anagram list 

Space Complexity:
O(n + q) , where n is the space required to store the key of the anagram and q for its matching
anagram in a list key -> list

--------------------------------------------------

Learnings:
Learned ways to combine sorting with dictionary and not everting can be solved in O(n)

Mistakes:
I am scared what if I can't solve the problem in O(n). May be not all problem can be solved 
in O(n), I need to overcome this with practice
"""
from collections import defaultdict

def groupAnagrams(strs):
    anagram_dict = defaultdict(list)
    anagram_group = []
    for word in strs:
        sorted_str = "".join(sorted(word))
        anagram_dict[sorted_str].append(word)
    
    for group in anagram_dict.values():
        anagram_group.append(group)
    
    return anagram_group

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))
