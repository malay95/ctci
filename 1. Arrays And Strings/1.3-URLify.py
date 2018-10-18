"""
URLify: write a method to replace all spaces in the string with %20
"""


def URLify(s):
    """
    :param s: string with enough space. in python we dont need this constraint as there is no constraint in the string ds
    :type s: str
    :return: string with replaced value
    :rtype: str
    """
    return s.replace(' ','%20')

assert URLify("Mr John Smith ") == "Mr%20John%20Smith%20"