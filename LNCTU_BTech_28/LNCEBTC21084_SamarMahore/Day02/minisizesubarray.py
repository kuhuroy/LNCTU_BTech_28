class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        summ = 0
        minimum = float('inf')

        for i in range(len(nums)):
            summ += nums[i]

            while summ >= target:
                minimum = min(minimum, i - start + 1)
                summ -= nums[start]
                start += 1

        if minimum == float('inf'):
            return 0
        return minimum



