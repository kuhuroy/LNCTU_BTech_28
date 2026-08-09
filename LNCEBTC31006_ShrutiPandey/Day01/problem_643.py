class Solution:
    def findMaxAverage(self, nums, k):
        # Calculate sum of the first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window through the array
        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]

            max_sum = max(max_sum, window_sum)

        return max_sum / k


# Example:
# nums = [1, 12, -5, -6, 50, 3]
# k = 4
# print(Solution().findMaxAverage(nums, k))