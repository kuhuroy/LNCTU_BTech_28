class NumArray:
    def __init__(self , nums):
        self.prefix = [0]
        

        for num in nums:
             self.prefix.append(self.prefix[-1]+num)

    def sumRange(self , left , right):
        return self.prefix[right+1] -self.prefix[left]         
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)