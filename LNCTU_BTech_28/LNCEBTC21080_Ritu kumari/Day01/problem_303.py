# Leetcode303-Range Sum Query Immutable
# Solution


class NumArray:


    def __init__(self, nums):
        # Prefix sum array
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        # Sum from left to right
        return self.prefix[right + 1] - self.prefix[left]


# Example
# Input: nums = [-2, 0, 3, -5, 2, -1]
# Query: left = 0, right = 2
# Output = 1, -1, -3