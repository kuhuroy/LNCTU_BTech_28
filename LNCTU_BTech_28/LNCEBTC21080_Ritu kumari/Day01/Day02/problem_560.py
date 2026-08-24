# LeetCode 560-Subarray Sum Equals K
# Solution

class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        seen = {0: 1}

        for value in nums:
            prefix_sum += value

            if prefix_sum - k in seen:
                count += seen[prefix_sum - k]

            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count




# Example:
# Input:nums = [1, 1, 1], k = 2
# Subarrays:[1, 1]and[1,1]
# Output = 2