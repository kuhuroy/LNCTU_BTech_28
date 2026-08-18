class NumArray:
    def __init__(self, nums):
        self.nums=nums
    def sumRange(self, left, right):
        result=sum(self.nums[left:right+1])
        return result        
nums=[1,2,3,4,5,6,7,8,9]
obj= NumArray(nums)
param_1 = obj.sumRange(1,2)
