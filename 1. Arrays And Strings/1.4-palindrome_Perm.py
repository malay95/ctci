"""
Palindrome Permutation: Given a string, write a function to check if its permutation of a palindrome.
A palindrome is a word ot phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters
"""


# Approach 1: create a dictionary that saves the count of each character and check if the max number of odd is 1
# Approach 2: represent the dictionary with bool instead of count and check number of true, approach 1 is more intuitive

def isPalindromePermutation_1(s):
    s = s.lower().replace(" ","") #lower case and removing space
    odd_count = 0
    count_dict = dict()
    for i in s:
        if i in count_dict:
            count_dict[i] += 1
            odd_count = odd_count - 1 if count_dict[i] % 2 == 0 else odd_count + 1
        else:
            count_dict[i] = 1
            odd_count += 1
    return odd_count <= 1

assert isPalindromePermutation_1("Tact Coa") is True
assert isPalindromePermutation_1("hello") is False

