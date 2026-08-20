# Leetcode2643-Row With Maximum Ones
# Solution

def rowAndMaximumOnes(mat):

    max_ones = 0
    row_index = 0

    for i in range(len(mat)):
        count = 0

        # Count number of 1s in each row
        for value in mat[i]:
            if value == 1:
                count += 1

        # Update maximum
        if count > max_ones:
            max_ones = count
            row_index = i

    return [row_index, max_ones]


# Example
#Input:
# mat = [
#    [0, 1],
#    [1, 1],
#    [1, 0]
# ]
#
# Row 0 has 1 one
# Row 1 has 2 ones
# Row 2 has 1 one
#
# Output:[1, 2]





