"""
Rotate Matrix: Given an image represented by NxN matrix, where each pixel in the image is 4 bytes, write a method to
rotate the image by 90 degrees. Do this in place.
"""


def rotateMatrix(m):
    """
    rotate matrix
    :param m: matrix
    :type m: list of list of integers
    :return: rotated matrix
    :rtype: list of list
    """
    for i in range(int(len(m) / 2)):
        last_layer = len(m) - i - 1
        for j in range(i, last_layer):
            offset = j - i
            top = m[i][j]
            m[i][j] = m[last_layer-offset][i]
            m[last_layer- offset][i] = m[last_layer][last_layer - offset]
            m[last_layer][last_layer - offset] = m[j][last_layer]
            m[j][last_layer] = top
    return m


assert rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [[13, 9, 5, 1], [14, 10, 6, 2],
                                                                                         [15, 11, 7, 3], [16, 12, 8, 4]]
