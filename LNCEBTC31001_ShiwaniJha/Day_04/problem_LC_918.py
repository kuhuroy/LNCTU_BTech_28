# optimal solution
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = nums[0] # total of arr
        curmaxi = maxi = nums[0] # curr and overall maxi & min
        curmini = mini = nums[0]
        for i in range(1, n):
            total = total + nums[i] # adding curr ele in total
            curmaxi = max(nums[i], curmaxi + nums[i]) # max subarr ending at curr ele
            maxi = max(maxi, curmaxi) # update overall maxi
            curmini = min(nums[i], curmini + nums[i]) # min subarr ending at curr ele
            mini = min(mini, curmini) # updating
        if maxi < 0: # all nums are neg, retrn largest num
            return maxi
        circular = total - mini # maxi circular sum = total - min subarr
        return max(circular, maxi) 

'''
918. Maximum Sum Circular Subarray
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
'''


# wrong but first attempt
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        maxi = nums[0]
        for i in nums:
            total = total + i
            if total > maxi:
                maxi = total
            if total < 0:
                total = 0
        return maxi
