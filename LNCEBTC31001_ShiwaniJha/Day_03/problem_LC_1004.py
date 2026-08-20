class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0 # maxi valid win len
        l = 0 # left ptr
        r = 0 # right ptr
        zeros = 0
        n = len(nums)
        while r < n: # until r* reaches end
            if nums[r] == 0: # Count 0 if cure ele is 0
                zeros+=1
            while zeros>k:  # If zeros exceed k, reduce window from left
                if nums[l]==0: # Removing leftmost 0 from the window
                    zeros-=1 # Remove it from zero count
                l+=1 # Move left ptr forward
            maxi = max(maxi, r-l+1) # Curr valid window length
            r+=1 # move r * to inc window
        return maxi 


'''
1004. Max Consecutive Ones III
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
 

'''
