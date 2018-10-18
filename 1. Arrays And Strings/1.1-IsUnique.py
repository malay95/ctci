"""
Is Unique- Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

#Approach 1 - compare the character with every other characters in the string. takes O(n_2)
#Approach 2 - sort the string and compare the adjacent characters

def IsUnique(s):
    """
    checks if the characters in the string are unique
    :param s: string to be compared
    :type s: str
    :return: true if the string has unique chars else false
    :rtype: bool
    """
    s = sorted(s)
    for i in range(len(s)):
        if i<len(s)-1 and s[i] == s[i+1]:
            return False
    return True

assert IsUnique("aabbcc") is False
assert IsUnique("abc") is True
