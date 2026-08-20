#  Solution

class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        n = len(nums)
        total = sum(nums[:k]) # it gives sum of 0th index to k-1th index, which is sum of first 'k' no. of elemenst
        maxi = total # will update until gets the maximum
        for i in range(k, n): # till (k-1)th already calculated so will check from k-th elemnt
            total = total - nums[i-k] + nums[i] # remove the first ele, and add next ele, and continue chekcing
            if total > maxi:
                maxi = total
        mean = maxi / k # calc the mean of maximum sum of k eles
        return mean

#  TC = O(N), SC = O(1)

'''
643. Maximum Average Subarray I
Solved
Easy
Topics
premium lock icon
Companies
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''
