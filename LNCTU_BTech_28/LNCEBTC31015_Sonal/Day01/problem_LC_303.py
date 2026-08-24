class NumArray:

    def __init__(self, nums):
        self.prefix = [0]

        for x in nums:
            self.prefix.append(self.prefix[-1] + x)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


# Input
nums = [-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)

print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
