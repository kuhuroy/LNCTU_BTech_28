class Solution:
    def rowAndMaximumOnes(self, mat):
        max_ones = 0
        row_index = 0

        for i in range(len(mat)):
            count = sum(mat[i])

            if count > max_ones:
                max_ones = count
                row_index = i

        return [row_index, max_ones]
