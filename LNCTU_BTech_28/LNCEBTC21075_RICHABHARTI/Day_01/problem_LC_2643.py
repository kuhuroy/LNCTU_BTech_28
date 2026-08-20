
#Problem: 2643.  Maximum Average Subarray


#Solution

class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum / k


# Example:
# nums = [1, 12, -5, -6, 50, 3]
# k = 4
# print(Solution().findMaxAverage(nums, k))  # 12.75
