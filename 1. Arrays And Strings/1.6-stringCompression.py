"""
String Compression: Implement a method to perform a basic string compression using counts of repeated characters.
For example the string aabcccccaaa would return a2bc5a3. If the compressed string contains a character which occurs once
don't add the count and don't use extra space
"""


def stringCompression(s):
    if s == "":
        return ""
    s = list(s)
    last_char = s[0]
    count = 1
    output_index = 0
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == last_char:
            count += 1
        else:
            if count == 1:
                s[output_index] = last_char
                output_index += 1
            else:
                s[output_index] = last_char
                s[output_index + 1] = str(count)
                output_index += 2
                count = 1
            last_char = s[i] if i < len(s) else s[0]
    return ''.join(s[:output_index])


assert stringCompression("aabcccccaaa") == "a2bc5a3"
assert stringCompression("abcd") == "abcd"
assert stringCompression("") == ""
assert stringCompression("aaaaa") == "a5"