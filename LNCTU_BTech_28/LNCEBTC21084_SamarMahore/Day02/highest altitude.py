class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result=[0]*(len(gain)+1)
        for i in range (1,len(result)):
            result[i]=result[i-1]+gain[i-1]
        return max(result)

        