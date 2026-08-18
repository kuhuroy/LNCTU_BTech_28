class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        minimum = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                minimum = min(minimum, right - left + 1)
                total -= nums[left]
                left += 1

        if minimum == float('inf'):
            return 0

        return minimum
