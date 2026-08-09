class NumArray:
    def __init__(self, nums):
        # Prefix sum array
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        # Calculate range sum using prefix sum
        return self.prefix[right + 1] - self.prefix[left]


# Example:
# nums = [-2, 0, 3, -5, 2, -1]
# obj = NumArray(nums)
# print(obj.sumRange(0, 2))