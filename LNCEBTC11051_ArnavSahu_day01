
# day-1 tasks
#LNCEBTC11051_ArnavSahu

   #problem_303.py
             
      class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        cur=0
        for n in nums:
            cur+=n
            self.prefix.append(cur)
        

    def sumRange(self, left: int, right: int) -> int:
        rightSum=self.prefix[right]
        LeftSum=self.prefix[left-1] if left>0 else 0
        return rightSum-LeftSum
        



  #problem_643.py
  
      class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        s=0
        for i in range(k):
            s+=nums[i]

        max_avg = s/k
        for i in range(k,n):
                s+=nums[i]
                s-=nums[i-k]
                avg = s/k
                max_avg=max(max_avg,avg)
        return max_avg
