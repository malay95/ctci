"""
String rotation: Assume you have a method isSubstring (in python 'in' operator) which checks if one word is a substring of another.
Given two string s1,s2 write code to check if s2 is a rotation of s1 using only one call to isSubstring
eg. "waterbottle" is a rotation of "erbottlewat"
"""

def stringRotation(s1,s2):
    concated_string = s1 + s1
    if s2 in concated_string:
        return True
    return False

assert stringRotation("waterbottle","erbottlewat") is True