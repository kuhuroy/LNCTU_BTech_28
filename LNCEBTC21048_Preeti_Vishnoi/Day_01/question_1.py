class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.sum = [0]
        for x in nums:
            self.sum.append(self.sum[-1] + x)

    def sumRange(self, left, right):
        return self.sum[right + 1] - self.sum[left]

