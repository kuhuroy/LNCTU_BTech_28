class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = []
        n =len(nums)
        i = 0    # left ptr
        total = 0 # curr window sum
        for j in range(n):   # right ptr
            total += nums[j] # add curr ele, add until you reach the condtn of total >= target
            while total >= target:
                res.append(j - i + 1) # store curr window len
                total -= nums[i] # removing the left most ele
                i += 1 # left ptr moves
        if res:
            return min(res) # return the min widow size
        else:
            return 0 

#  TC = O(N)
#  SC = O(1)


'''
209. Minimum Size Subarray Sum
Solved
Medium
Topics
premium lock icon
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

'''
