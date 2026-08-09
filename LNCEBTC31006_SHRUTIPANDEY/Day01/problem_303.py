class NumArray:

    def __init__(self, nums):
        # Store prefix sums to answer range sum quickly
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        # Sum from left to right using prefix sum
        return self.prefix[right + 1] - self.prefix[left]


# Example
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)

print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))