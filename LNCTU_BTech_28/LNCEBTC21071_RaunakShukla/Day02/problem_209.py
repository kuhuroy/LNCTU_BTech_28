class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        summ=0
        mini=float('inf')
        for i in range(len(nums)):
            summ+=nums[i]
            while summ>=target:
                mini=min(mini,i-start+1)
                summ-=nums[start]
                start+=1
        if mini == float('inf' ):
             return 0
        else :
            return miniclass Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        summ=0
        mini=float('inf')
        for i in range(len(nums)):
            summ+=nums[i]
            while summ>=target:
                mini=min(mini,i-start+1)
                summ-=nums[start]
                start+=1
        if mini == float('inf' ):
             return 0
        else :
            return mini