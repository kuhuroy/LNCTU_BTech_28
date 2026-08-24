
#Problem: 303. Range Sum Query - Immutable

#Solution

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.sum = [0]
        for x in nums:
            self.sum.append(self.sum[-1] + x)

    def sumRange(self, left, right):
        return self.sum[right + 1] - self.sum[left]


# Example:
# nums = [-2, 0, 3, -5, 2, -1]
# obj = NumArray(nums)
# print(obj.sumRange(0, 2))









