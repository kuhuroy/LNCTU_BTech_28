class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


# Taking input
nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

# Create object
obj = Solution()

# Print answer
print("Maximum Average:", obj.findMaxAverage(nums, k))
