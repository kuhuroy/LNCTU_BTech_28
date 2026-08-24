class Solution:
    def findMaxAverage(self, nums, k):
        total = 0

        for i in range(k):
            total += nums[i]
        max_sum = total

        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i - k]
            if total > max_sum:
                max_sum = total

        return max_sum / k