"""
Write an algorithm such that if an element in an MxM matrix is 0, its entire row and column are set to 0
"""

# Approach 1: keep a list for rows and columns that have zeros as values
# Approach 2: keep the first row of the matrix as the space for keeping the column and rows with zeros
def zeroMatrix_1(m):
    row = set()
    column = set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                row.add(i)
                column.add(j)
    for i in row:
        m[i] = [0 for x in range(len(m[i]))]
    for i in column:
        for j in range(len(m[0])):
            m[j][i] = 0
    return m

def zeroMatrix_2(m):
    row_flag = True if 0 in m[0] else False
    column_flag = True if 0 in [x[0] for x in m] else False
    for i in range(1,len(m)):
        for j in range(1,len(m[i])):
            if m[i][j] == 0:
                m[i][0] = 0
                m[0][j] = 0
    for i in range(1,len(m[0])):
        if m[0][i] == 0:
            for j in range(len(m)):
                m[j][i] = 0
    for i in range(1,len(m[0])):
        if m[i][0] == 0:
            for j in range(len(m)):
                m[i][j] = 0
    if row_flag:
        for i in range(len(m)):
            m[i][0] = 0
    if column_flag:
        for i in range(len(m)):
            m[0][i] = 0
    return m

assert zeroMatrix_1([[1,2],[2,0]]) == [[1,0],[0,0]]
assert zeroMatrix_1([[1,2,3,4],[5,0,6,7],[8,9,1,0],[2,3,4,5]]) == [[1,0,3,0],[0,0,0,0],[0,0,0,0],[2,0,4,0]]

assert zeroMatrix_2([[1,2],[2,0]]) == [[1,0],[0,0]]
assert zeroMatrix_2([[1,2,3,4],[5,0,6,7],[8,9,1,0],[2,3,4,5]]) == [[1,0,3,0],[0,0,0,0],[0,0,0,0],[2,0,4,0]]