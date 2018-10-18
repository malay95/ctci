"""
Check Permutation: Given two strings write a method to decide if one is a permutation of the other
"""

# Approach - 1: sort both the strings and check for equality.
# Space complexity- O(1) and time - O(log n) where n is the len of the largest string

def checkPermutation(a,b):
    a = sorted(a)
    b = sorted(b)
    if a==b:
        return True
    else:
        return False

assert checkPermutation("abc","bac") is True
assert checkPermutation("aab","ab") is False
