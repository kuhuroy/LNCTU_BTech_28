# Method - 1 [Brute Force]
class NumArray:
    def __init__(self, nums):
        self.nums = nums  
    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right+1):
            res += self.nums[i]
        return res
#  TC = O(N), SC = O(1)



#  Method - 2 [ Optimal] 
class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.prefix = [0]
        for i in nums:
            self.prefix.append(self.prefix[-1] + i)
    def sumRange(self, left: int, right: int) -> int:
        res = self.prefix[right+1] - self.prefix[left]
        return res
#  TC = O(1)
#  SC = O(N)

#  Testing-
# nums = [3, 6, -3, 7, -2, 5]    
# obj = NumArray(nums)
# param_1 = obj.sumRange(1, 4)
# print(param_1)

'''explanation:
stored the prefix sum for all element- 
ex: [2, 5, -1, 8] prefix = [0, 2, 7, 6, 14]
now to get sum from left to right range of (1,2)
return the prefix[r+1] - prefrix[l] = p[3] - p[1]= 6-2 = 4
see, nums[1] + nums[2] = 5 -1 = 4
this gives optimal soln as we have tc of o(1) 
in trade of sc which is now o(n).
'''

'''
303. Range Sum Query - Immutable
Solved
Easy
Topics
premium lock icon
Companies
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.
'''
