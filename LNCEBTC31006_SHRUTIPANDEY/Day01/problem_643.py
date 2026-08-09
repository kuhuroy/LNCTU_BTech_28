class Solution:
    def findMaxAverage(self, nums, k):
        # Find the sum of the first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Move the window one step at a time
        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]

            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k


# Example
nums = [1, 12, -5, -6, 50, 3]
k = 4
solution = Solution()
print(solution.findMaxAverage(nums, k))