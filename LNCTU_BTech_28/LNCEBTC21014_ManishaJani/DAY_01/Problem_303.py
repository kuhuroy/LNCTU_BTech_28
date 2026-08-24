class NumArray:

    def __init__(self, nums):
        self.prefix = [0]

        for x in nums:
            self.prefix.append(self.prefix[-1] + x)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]