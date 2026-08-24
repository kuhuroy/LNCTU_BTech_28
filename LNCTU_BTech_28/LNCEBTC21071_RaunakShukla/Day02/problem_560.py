class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        summ = 0
        freq = {0: 1}

        for num in nums:
            summ += num

            if summ - k in freq:
                count += freq[summ - k]

            freq[summ] = freq.get(summ, 0) + 1

        return count