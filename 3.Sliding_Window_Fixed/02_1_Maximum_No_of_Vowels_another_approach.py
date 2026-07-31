'''

This is an another approach, after I found the solution using my approach, because I have used 
a lot of if else block, I wan thinking how can i Improve the code and do it in a more pythonic
way. So with some help from the internet this is what I came up with.

'''

def maxVowels(s, k):
    vowels = {"a","e","i","o","u"}
    current_vowels = sum(1 for char in s[:k] if char in vowels)
    max_vowels = current_vowels

    for right in range(k,len(s)):
        left_char = s[right-k]
        right_char = s[right]

        current_vowels += (right_char in vowels) - (left_char in vowels)
            
        if current_vowels > max_vowels:
            max_vowels = current_vowels

    return max_vowels

s = "abciiidef"
k = 3

print(maxVowels(s,k))