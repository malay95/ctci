"""
One-Way: There are three types of edits that can be performed in on strings: insert, remove and replace.
Given 2 strings, write a function to check if they are one edit(or zero edit) away.
"""


def oneWay(a, b):
    long = a if len(a) >= len(b) else b
    short = a if len(a) < len(b) else b
    flag = False
    long_index = short_index = 0
    while long_index < len(long) and short_index < len(short):
        if long[long_index] != short[short_index]:
            if flag:
                return False
            else:
                # case of insertion or removal
                flag = True
            if len(long) == len(short):
                # case of replace
                short_index += 1
        else:
            short_index += 1
        long_index += 1
    return True


assert oneWay("pale", "ple") is True
assert oneWay("pales", "pale") is True
assert oneWay("pale", "bale") is True
assert oneWay("pale", "bae") is False
