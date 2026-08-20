# Leetcode209-Minium Size Subarray Sum
# Solution


class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        window_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length



    # Example
    # Input:target = 7, nums = [2, 3, 1, 2, 4, 3]
    # Smallest subarray:[4, 3 ]
    # Output = 2


 
    