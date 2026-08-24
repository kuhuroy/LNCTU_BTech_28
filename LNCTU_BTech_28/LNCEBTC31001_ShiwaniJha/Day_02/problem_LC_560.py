class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            total = 0 # reset the total of each start
            for j in range(i, n): # end index
                total += nums[j] # add curr ele
                if total == k:
                    count += 1
        return count

# Time: O(n²) 
# Space: O(1)
#  TLE ERROR

#  OPTIMAL Solution
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1} # start me prefix sum is 0 
        total = 0
        count = 0
        for i in nums:
            total = total + i # curr preifx sum
            if total - k in freq: # already exist
                count += freq[total - k] # subarray with sum "k" found, count inc
            if total in freq:
                freq[total] += 1 # inc freq
            else:
                freq[total] = 1 # new prefix sum # total count
        return count 

#  Time Complexity: O(n)
# Space Complexity: O(n)

'''
560. Subarray Sum Equals K
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


'''
