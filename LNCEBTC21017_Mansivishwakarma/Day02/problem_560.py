class Solution:
    def subarraySum(self, nums, k):
        count = 0
        total = 0
        mp = {0: 1}

        for num in nums:
            total += num

            if total - k in mp:
                count += mp[total - k]

            mp[total] = mp.get(total, 0) + 1

        return count
