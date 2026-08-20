#  Brute force solution
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mini = float('inf')
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= k:
                    mini = min(mini, j-i+1)
                    break
        if mini == float('inf'):
            return -1
        else:
            return mini

#  Optimal solution
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]* (n+1)   # Creating prefix sum
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        dq = deque()  # Store useful prefix indices
        ans = n+1  # Store shortest len
        for j in range(n+1):
            while dq and prefix[j] - prefix[dq[0]] >= k :    # Check if curr sum is at least k
                ans = min(ans, j - dq[0])  # Calculate subarr len
                dq.popleft()  # Remove front after finding a valid subarr
            while dq and prefix[j] <= prefix[dq[-1]]:  # Remove useless larger prefix sums
                dq.pop()
            dq.append(j) # Add curr prefix index
        if ans == n+1:  # Return -1 if no valid subarr was found
            return -1
        return ans

# Time: O(n)
# Space: O(n)


'''
862. Shortest Subarray with Sum at Least K
Solved
Hard
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109

'''
